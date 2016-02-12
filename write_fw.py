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

import parse_rdesc
import sys
import struct
import binascii

class FW(object):
	def __init__(self, filename):
		self.filename = filename
		self.fd = open(filename, "wb")
		self.content = b''

	def write(self, data):
		self.fd.write(data)
		self.content += data

	def dump_string(self, prefix, string):
		self.write(struct.pack('c', prefix))
		self.write(struct.pack('i', len(string) + 1)) # for terminating 0
		self.write(struct.pack('{0}s'.format(len(string) + 1), string))

	def dump_rdesc(self, data, prefix):
		if len(prefix) > 1:
			raise Exception, "Invalid prefix: %s"%prefix
		rdesc = parse_rdesc.parse_rdesc(data, None)
		if not rdesc:
			raise IOError
		self.write(struct.pack('c', prefix))
		self.write(struct.pack('i', rdesc.size()))
		for b in rdesc.data():
			self.write(struct.pack('B', b))

	def dump_int(self, prefix, value):
		if len(prefix) > 1:
			raise Exception, "Invalid prefix: %s"%prefix
		self.write(struct.pack('c', prefix))
		self.write(struct.pack('i', 4))
		self.write(struct.pack('i', value))

	def append_crc(self):
		# match the in-kernel crc32 function
		crc = ~binascii.crc32(self.content, 0xffffffff) & 0xffffffff
		self.fd.write(struct.pack('I', crc))

	def close(self):
		self.fd.close()
		self.fd = None

def main():
	output = open("out.bin", "wb")

	for filename in sys.argv[1:]:
		f = open(filename)
		for line in f.readlines():
			if line.startswith("R:"):
				dump_rdesc(line.lstrip("R: "), "R", output)
			elif line.startswith("O:"):
				dump_rdesc(line.lstrip("O: "), "O", output)

	output.close()

if __name__ == "__main__":
	main()
