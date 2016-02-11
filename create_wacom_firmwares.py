#!/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014-2016 Benjamin Tissoires <benjamin.tissoires@gmail.com>
# Copyright (c) 2014-2016 Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import sys
import subprocess
import shlex
import re
sys.path.append(os.path.join(os.getcwd(), "hid-replay", "tools"))
import hid
import parse_rdesc
import parse_hid
import devices
import write_fw

class Wacom(devices.Wacom):
	def __init__(self, wac_object):
		self.name = wac_object.name
		self.reports = wac_object.reports
		self.logical_mins = self.lower_dict(wac_object.logical_mins)
		self.logical_maxs = self.lower_dict(wac_object.logical_maxs)
		self.physical_mins = self.lower_dict(wac_object.physical_mins)
		self.physical_maxs = self.lower_dict(wac_object.physical_maxs)

		self.product_id = wac_object.product_id
		self.original_reports = wac_object.original_reports

		self.rdesc = parse_rdesc.ReportDescriptor()
		self.raw_rdesc = []

		self.__complete_min_max()

	def fw_filename(self):
		return "0003_056a_{0:04x}.bin".format(self.product_id)

	def hid_filename(self):
		return "0003_056a_{0:04x}.hid".format(self.product_id)

	def get_canonical_name(self):
		name = self.name
		m = re.match(r"(.*) Pen$", name)
		if m:
			name = m.group(1)
		m = re.match(r"(.*) Pad$", name)
		if m:
			name = m.group(1)
		m = re.match(r"(.*) Finger$", name)
		if m:
			name = m.group(1)
		return name

	def lower_dict(self, dictionary):
		d = {}
		for key, v in dictionary.items():
			d[key.lower()] = v
		return d

	def get_min_max(self, usage_name, min_max_list):
		n = usage_name.lower()
		if n in min_max_list.keys():
			return min_max_list[n]
		return 0

	def get_logical_max(self, usage_name, size, min_max_list):
		max = self.get_min_max(usage_name, min_max_list)
		if not max:
			max = (1 << size) - 1
		return max

	def __check_min_max(self, usage, size):
		usage = parse_hid.get_usage(usage)
		usage = usage.split(" << ")[0]
		lmin = self.get_min_max(usage, self.logical_mins)
		lmax = self.get_logical_max(usage, size, self.logical_maxs)
		pmin = self.get_min_max(usage, self.physical_mins)
		pmax = self.get_min_max(usage, self.physical_maxs)
		return lmin, lmax, pmin, pmax

	def create_min_max(self, tag, n):
		tag = hid.hid_items["Global"][tag]
		size = 1
		items = [ n & 0xff]
		n >>= 8
		if n:
			size = 2
			items.append(n & 0xff)
			n >>= 8
		if n:
			size = 3
			items.append(n & 0xff)
			n >>= 8
			items.append(n & 0xff)
		items.insert(0, tag | size)
		return items

	def create_unit(self):
		items = [
			0x55, 0x0e, # Unit Exponent (-2)
			0x65, 0x11, # Unit (Centimeter,SILinear)
			]
		return items


	def __complete_min_max(self):
		i = 0
		usage = 0
		usage_min = 0
		usage_max = 0
		current_l_min = 0
		current_l_max = 0
		current_p_min = 0
		current_p_max = 0
		override = False
		for report in self.reports:
			for value in report:
				item = self.rdesc.consume(value, i)
				i += 1
				if not item:
					continue
				if item.item == "Usage":
					usage = self.rdesc.usage[-1]
				elif item.item == "Usage Minimum":
					usage_min = self.rdesc.usage_min
				elif item.item == "Usage Maximum":
					usage_max = self.rdesc.usage_max
				elif item.item == "Logical Minimum":
					current_l_min = item.value
					override = True
				elif item.item == "Logical Maximum":
					current_l_max = item.value
					override = True
				elif item.item == "Physical Minimum":
					current_p_min = item.value
					override = True
				elif item.item == "Physical Maximum":
					current_p_max = item.value
					override = True
				elif item.item == "Input" and (item.value & 0x01) == 0:
					if usage_min and usage_max:
						usage = usage_min
					lmin, lmax, pmin, pmax = self.__check_min_max(usage, self.rdesc.item_size)
					if not override:
						if current_l_min != lmin or current_l_max != lmax:
							self.raw_rdesc.extend(self.create_min_max("Logical Minimum", lmin))
							self.raw_rdesc.extend(self.create_min_max("Logical Maximum", lmax))
							current_l_min = lmin
							current_l_max = lmax
						if current_p_min != pmin or current_p_max != pmax:
							self.raw_rdesc.extend(self.create_unit())
							self.raw_rdesc.extend(self.create_min_max("Physical Minimum", pmin))
							self.raw_rdesc.extend(self.create_min_max("Physical Maximum", pmax))
							current_p_min = pmin
							current_p_max = pmax
					override = False
					usage_min = 0
					usage_max = 0
				self.raw_rdesc.append(item.r)
				self.raw_rdesc.extend(item.raw_value)
		self.rdesc = parse_rdesc.ReportDescriptor()
		i = 0
		for value in self.raw_rdesc:
			self.rdesc.consume(value, i)
			i += 1

def get_version():
	process = subprocess.Popen(shlex.split("git describe --tags --dirty=+"),
				   stdout=subprocess.PIPE,
				   stderr=subprocess.PIPE)
	out, err = process.communicate()
	errcode = process.returncode

	if errcode:
		return None

	return out.rstrip("\n")


def dump_hid(wac_object, outfile, n):
	outfile.write("D: {0}\n".format(n))
	outfile.write("N: {0} ".format(wac_object.name))
	outfile.write('\n')
	if wac_object.original_reports:
		outfile.write("O: {0}\n".format(wac_object.original_reports))
	outfile.write("R: {0} ".format(wac_object.rdesc.size()))
	wac_object.rdesc.dump_raw(outfile)
	outfile.write('\n')

def main():
	output_dir = "output"
	version = get_version()
	print "Will mark the following firmwares with version '{0}'".format(version)
	if not os.path.exists(output_dir):
		os.mkdir(output_dir)
	for items in devices.Wacom.all_items.values():
		cleaned_object = Wacom(items[0])
		hid_name = os.path.join(output_dir, cleaned_object.hid_filename())
		fw_name = os.path.join(output_dir, cleaned_object.fw_filename())
		print "dumping", hid_name, "for",  ", ".join([ o.name for o in items])
		f_hid = open(hid_name, "w")
		print "writing", fw_name, "for",  ", ".join([ o.name for o in items])
		f_bin = write_fw.FW(fw_name)
		f_bin.dump_string("V", version)
		f_bin.dump_string("N", cleaned_object.get_canonical_name())
		i = 0
		for o in items:
			cleaned_object = Wacom(o)
			dump_hid(cleaned_object, f_hid, i)
			if cleaned_object.original_reports:
				f_bin.dump_rdesc(cleaned_object.original_reports, "O")
			data = str(cleaned_object.rdesc.size()) + " " + cleaned_object.rdesc.data_txt()
			f_bin.dump_rdesc(data, "R")
			i += 1
		f_bin.append_crc()
		f_hid.close()
		f_bin.close()

if __name__ == "__main__":
	main()
