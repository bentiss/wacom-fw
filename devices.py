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

from descriptors import *

class Wacom(object):
	all_items = {}
	def __init__(self, name, product_id, reports,
			logical_mins, logical_maxs,
			physical_mins, physical_maxs, original_reports = None):
		self.name = name
		self.product_id = product_id
		self.reports = reports
		self.original_reports = original_reports
		self.logical_mins = logical_mins
		self.logical_maxs = logical_maxs
		self.physical_mins = physical_mins
		self.physical_maxs = physical_maxs
		if not Wacom.all_items.has_key(product_id):
			Wacom.all_items[product_id] = []
		Wacom.all_items[product_id].append(self)

cintiq_22HD_pen = Wacom(
	name = "Wacom Cintiq 22HD Pen",
	product_id = 0x00fa,
	reports = (
		boot_mouse_collection,
		device_id_report_intuos3,
		generic_stylus_intuos4,
		airbrush_report_inutos4,
		artpen_report_intuos4,
		express_keys_touch_strip_cintiq_22HD,
	),
	logical_mins = {
		"Z": -900,
	},
	logical_maxs = {
		"X": 95840,
		"Y": 65600,
		"Z": 899,
		"RX": 4096,
		"RY": 4096,
		"Wheel": 1023,
		"Tip Pressure": 2047,
		"Altitude": 63,
		"X Tilt": 127,
		"Y Tilt": 127,
	},
	physical_mins = {
	},
	physical_maxs = {
		"X": 4792,
		"Y": 2713,
	}
)

cintiq_22HDT_pen = Wacom(
	name = "Wacom Cintiq 22HDT Pen",
	product_id = 0x005b,
	reports = (
		boot_mouse_collection,
		device_id_report_intuos3,
		generic_stylus_intuos4,
		airbrush_report_inutos4,
		artpen_report_intuos4,
		express_keys_touch_strip_cintiq_22HD,
	),
	logical_mins = {
		"Z": -900,
	},
	logical_maxs = {
		"X": 95840,
		"Y": 65600,
		"Z": 899,
		"RX": 4096,
		"RY": 4096,
		"Wheel": 1023,
		"Tip Pressure": 2047,
		"Altitude": 63,
		"X Tilt": 127,
		"Y Tilt": 127,
	},
	physical_mins = {
	},
	physical_maxs = {
		"X": 4792,
		"Y": 2713,
	}
)

cintiq_24HDT_pen = Wacom(
	name = "Wacom Cintiq 24HDT Pen",
	product_id = 0x00f8,
	reports = (
		boot_mouse_collection,
		device_id_report_intuos3,
		generic_stylus_intuos4,
		airbrush_report_inutos4,
		artpen_report_intuos4,
		express_keys_touch_ring_cintiq_24HD,
	),
	logical_mins = {
		"Z": -900,
	},
	logical_maxs = {
		"X": 104480,
		"Y": 65600,
		"Z": 899,
		"RX": 4096,
		"RY": 4096,
		"Wheel": 1023,
		"Tip Pressure": 2047,
		"Altitude": 63,
		"X Tilt": 127,
		"Y Tilt": 127,
	},
	physical_mins = {
	},
	physical_maxs = {
		"X": 5224,
		"Y": 3280,
	}
)

intuos_5_S_pen = Wacom(
	name = "Wacom Intuos5 touch S Pen",
	product_id = 0x0026,
	reports = (
		boot_mouse_collection,
		device_id_report_intuos3,
		generic_stylus_intuos4,
		airbrush_report_inutos4,
		artpen_report_intuos4,
		five_button_mouse_report_intuos4,
		express_keys_touch_ring_intuos5_s,
		led_configuration_intuos5,
	),
	logical_mins = {
		"Z": -900,
	},
	logical_maxs = {
		"X": 31496,
		"Y": 19685,
		"Z": 899,
		"Wheel": 1023,
		"Tip Pressure": 2047,
		"Altitude": 63,
		"X Tilt": 127,
		"Y Tilt": 127,
	},
	physical_mins = {
	},
	physical_maxs = {
		"X": 1575,
		"Y": 984,
	},
	original_reports = "243 05 01 09 02 a1 01 85 01 09 01 a1 00 05 09 19 01 29 03 15 00 25 01 95 03 75 01 81 02 95 05 81 03 05 01 09 30 09 31 09 38 15 81 25 7f 75 08 95 03 81 06 c0 c0 05 0d 09 01 a1 01 85 02 09 00 75 08 96 09 00 15 00 26 ff 00 81 02 85 03 09 00 75 08 96 09 00 15 00 26 ff 00 81 02 85 c0 09 00 75 08 96 09 00 15 00 26 ff 00 81 02 85 02 09 00 95 01 b1 02 85 03 09 00 95 09 b1 02 85 05 09 00 95 08 b1 02 85 07 09 00 95 0f b1 02 85 08 09 00 95 04 b1 02 85 0a 09 00 95 02 b1 02 85 0b 09 00 95 01 b1 02 85 20 09 00 95 08 b1 02 85 04 09 00 95 01 b1 02 85 0d 09 00 95 01 b1 02 85 cc 09 00 95 02 b1 02 85 30 09 00 95 1f b1 02 85 31 09 00 95 04 b1 02 85 15 09 00 95 0a b1 02 85 14 09 00 95 0f b1 02 85 40 09 00 95 02 b1 02 85 dd 09 00 95 01 b1 02 c0"
)

intuos_Pro_S_pen = Wacom(
	name = "Wacom Intuos Pro S Pen",
	product_id = 0x0314,
	reports = (
		boot_mouse_collection,
		device_id_report_intuos3,
		generic_stylus_intuos4,
		airbrush_report_inutos4,
		artpen_report_intuos4,
		five_button_mouse_report_intuos4,
		express_keys_touch_ring_intuos5_s,
		led_configuration_intuos5,
	),
	logical_mins = {
		"Z": -900,
	},
	logical_maxs = {
		"X": 31496,
		"Y": 19685,
		"Z": 899,
		"Wheel": 1023,
		"Tip Pressure": 2047,
		"Altitude": 63,
		"X Tilt": 127,
		"Y Tilt": 127,
	},
	physical_mins = {
	},
	physical_maxs = {
		"X": 1575,
		"Y": 984,
	},
	original_reports = "234 06 0d ff 09 01 a1 01 85 02 09 00 75 08 96 09 00 15 00 26 ff 00 81 02 85 03 09 00 75 08 96 09 00 15 00 26 ff 00 81 02 85 c0 09 00 75 08 96 09 00 15 00 26 ff 00 81 02 85 02 09 00 95 01 b1 02 85 03 09 00 95 09 b1 02 85 05 09 00 95 08 b1 02 85 07 09 00 95 0f b1 02 85 08 09 00 95 04 b1 02 85 0a 09 00 95 02 b1 02 85 0b 09 00 95 01 b1 02 85 20 09 00 95 08 b1 02 85 04 09 00 95 01 b1 02 85 0d 09 00 95 01 b1 02 85 cc 09 00 95 02 b1 02 85 30 09 00 95 1f b1 02 85 31 09 00 95 04 b1 02 85 15 09 00 95 0a b1 02 85 14 09 00 95 0f b1 02 85 16 09 00 95 01 b1 02 85 40 09 00 95 02 b1 02 85 dd 09 00 95 01 b1 02 85 b0 09 00 95 02 b1 02 85 b1 09 00 96 09 01 b1 02 85 b2 09 00 96 08 01 b1 02 85 b3 09 00 95 01 b1 02 c0"
)

intuos_Pro_S_touch = Wacom(
	name = "Wacom Intuos Pro S Finger",
	product_id = 0x0314,
	reports = (
		bpt3_touch_msg_header,
		bpt3_touch_msg_finger,
		bpt3_touch_msg_finger,
		bpt3_touch_msg_finger,
		bpt3_touch_msg_finger,
		bpt3_touch_msg_finger,
		bpt3_touch_msg_finger,
		bpt3_touch_msg_finger,
		bpt3_touch_msg_footer,
	),
	logical_mins = {
	},
	logical_maxs = {
		"X": 4096,
		"Y": 4096,
		"Width": 4096,
		"Height": 4096,
	},
	physical_mins = {
	},
	physical_maxs = {
		"X": 1575,
		"Y": 984,
	},
	original_reports = "23 06 00 ff 09 01 a1 01 85 02 09 01 15 00 26 ff 00 75 08 95 3f 81 02 c0"
)

bambo_cth470_S_pen = Wacom(
	name = "Wacom Bamboo 16FG 4x5 Pen",
	product_id = 0x00de,
	reports = (
		bpt3_boot_mouse_collection,
		bpt3_pen_msg,
	),
	logical_mins = {
	},
	logical_maxs = {
		"X": 14720,
		"Y": 9200,
		"Tip Pressure": 1023,
		"Z": 31,
	},
	physical_mins = {
	},
	physical_maxs = {
		"X": 1575,
		"Y": 984,
	},
	original_reports = "92 05 01 09 02 a1 01 85 01 09 01 a1 00 05 09 19 01 29 05 15 00 25 01 95 05 75 01 81 02 95 01 75 03 81 01 05 01 09 30 09 31 15 81 25 7f 75 08 95 02 81 06 c0 c0 05 0d 09 01 a1 01 85 02 a1 00 06 00 ff 09 01 15 00 26 ff 00 75 08 95 09 81 02 c0 09 01 85 02 95 01 b1 02 09 01 85 03 95 01 b1 02 09 01 85 04 95 01 b1 02 09 01 85 05 95 01 b1 02 09 01 85 10 95 02 b1 02 09 01 85 11 95 10 b1 02 09 01 85 13 95 01 b1 02 09 01 85 20 95 01 b1 02 09 01 85 21 95 01 b1 02 09 01 85 14 95 1f b1 02 09 01 85 30 95 1f b1 02 09 01 85 31 95 04 b1 1f 85 c0 09 00 95 09 81 02 c0",
)

bambo_cth470_S_touch = Wacom(
	name = "Wacom Bamboo 16FG 4x5 Finger",
	product_id = 0x00de,
	reports = (
		bpt3_touch_msg_header,
		bpt3_touch_msg_finger,
		bpt3_touch_msg_finger,
		bpt3_touch_msg_finger,
		bpt3_touch_msg_finger,
		bpt3_touch_msg_finger,
		bpt3_touch_msg_finger,
		bpt3_touch_msg_finger,
		bpt3_touch_msg_footer,
	),
	logical_mins = {
	},
	logical_maxs = {
		"X": 4096,
		"Y": 4096,
		"Width": 4096,
		"Height": 4096,
	},
	physical_mins = {
	},
	physical_maxs = {
		"X": 1575,
		"Y": 984,
	},
	original_reports = "29 06 00 ff 09 80 a1 02 85 02 75 08 95 3f 15 00 26 00 10 81 01 85 03 75 08 95 3f 81 01 c0",
)
