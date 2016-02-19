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
	tag_pen = 1
	tag_touch = 2
	all_items = {}
	def __init__(self, name, product_id, reports,
			logical_mins, logical_maxs,
			physical_mins, physical_maxs,
			original_reports = None,
			sibling_device = None,
			tag = None):
		self.name = name
		self.product_id = product_id
		self.reports = reports
		self.original_reports = original_reports
		self.logical_mins = logical_mins
		self.logical_maxs = logical_maxs
		self.physical_mins = physical_mins
		self.physical_maxs = physical_maxs
		self.sibling_device = sibling_device
		self.tag = tag
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
		"Twist": -900,
	},
	logical_maxs = {
		"X": 95840,
		"Y": 65600,
		"Twist": 899,
		"RX": 4096,
		"RY": 4096,
		"Wheel": 1023,
		"Tip Pressure": 2047,
		"Altitude": 63,
		"X Tilt": 127,
		"Y Tilt": 127,
	},
	physical_mins = {
		"X Tilt": -64,
		"Y Tilt": -64,
	},
	physical_maxs = {
		"Twist": 359,
		"X Tilt": 63,
		"Y Tilt": 63,
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
		"Twist": -900,
	},
	logical_maxs = {
		"X": 95840,
		"Y": 65600,
		"Twist": 899,
		"RX": 4096,
		"RY": 4096,
		"Wheel": 1023,
		"Tip Pressure": 2047,
		"Altitude": 63,
		"X Tilt": 127,
		"Y Tilt": 127,
	},
	physical_mins = {
		"X Tilt": -64,
		"Y Tilt": -64,
	},
	physical_maxs = {
		"Twist": 359,
		"X Tilt": 63,
		"Y Tilt": 63,
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
		"Twist": -900,
	},
	logical_maxs = {
		"X": 104480,
		"Y": 65600,
		"Twist": 899,
		"RX": 4096,
		"RY": 4096,
		"Wheel": 1023,
		"Tip Pressure": 2047,
		"Altitude": 63,
		"X Tilt": 127,
		"Y Tilt": 127,
	},
	physical_mins = {
		"X Tilt": -64,
		"Y Tilt": -64,
	},
	physical_maxs = {
		"Twist": 359,
		"X Tilt": 63,
		"Y Tilt": 63,
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
		"Twist": -900,
	},
	logical_maxs = {
		"X": 31496,
		"Y": 19685,
		"Twist": 899,
		"Wheel": 1023,
		"Tip Pressure": 2047,
		"Altitude": 63,
		"X Tilt": 127,
		"Y Tilt": 127,
	},
	physical_mins = {
		"X Tilt": -64,
		"Y Tilt": -64,
	},
	physical_maxs = {
		"Twist": 359,
		"X Tilt": 63,
		"Y Tilt": 63,
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
		"Twist": -900,
	},
	logical_maxs = {
		"X": 31496,
		"Y": 19685,
		"Twist": 899,
		"Wheel": 1023,
		"Tip Pressure": 2047,
		"Altitude": 63,
		"X Tilt": 127,
		"Y Tilt": 127,
	},
	physical_mins = {
		"X Tilt": -64,
		"Y Tilt": -64,
	},
	physical_maxs = {
		"Twist": 359,
		"X Tilt": 63,
		"Y Tilt": 63,
		"X": 1575,
		"Y": 984,
	},
	original_reports = "234 06 0d ff 09 01 a1 01 85 02 09 00 75 08 96 09 00 15 00 26 ff 00 81 02 85 03 09 00 75 08 96 09 00 15 00 26 ff 00 81 02 85 c0 09 00 75 08 96 09 00 15 00 26 ff 00 81 02 85 02 09 00 95 01 b1 02 85 03 09 00 95 09 b1 02 85 05 09 00 95 08 b1 02 85 07 09 00 95 0f b1 02 85 08 09 00 95 04 b1 02 85 0a 09 00 95 02 b1 02 85 0b 09 00 95 01 b1 02 85 20 09 00 95 08 b1 02 85 04 09 00 95 01 b1 02 85 0d 09 00 95 01 b1 02 85 cc 09 00 95 02 b1 02 85 30 09 00 95 1f b1 02 85 31 09 00 95 04 b1 02 85 15 09 00 95 0a b1 02 85 14 09 00 95 0f b1 02 85 16 09 00 95 01 b1 02 85 40 09 00 95 02 b1 02 85 dd 09 00 95 01 b1 02 85 b0 09 00 95 02 b1 02 85 b1 09 00 96 09 01 b1 02 85 b2 09 00 96 08 01 b1 02 85 b3 09 00 95 01 b1 02 c0"
)

intuos_Pro_S_pen_wl = Wacom(
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
		led_configuration_intuos5_wl,
	),
	logical_mins = {
		"Twist": -900,
	},
	logical_maxs = {
		"X": 31496,
		"Y": 19685,
		"Twist": 899,
		"Wheel": 1023,
		"Tip Pressure": 2047,
		"Altitude": 63,
		"X Tilt": 127,
		"Y Tilt": 127,
	},
	physical_mins = {
		"X Tilt": -64,
		"Y Tilt": -64,
	},
	physical_maxs = {
		"Twist": 359,
		"X Tilt": 63,
		"Y Tilt": 63,
		"X": 1575,
		"Y": 984,
	},
	tag = Wacom.tag_pen,
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

intuos_Pro_S_touch_wl = Wacom(
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
	tag = Wacom.tag_touch,
)

bambo_cth470_S_pen = Wacom(
	name = "Wacom Bamboo 16FG 4x5 Pen",
	product_id = 0x00de,
	reports = (
		bpt3_boot_mouse_collection,
		bpt3_pen_msg,
		force_indirect_device,
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
		"X": 1475,
		"Y": 924,
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

cintiq_13HDT_pen = Wacom(
	name = "Wacom Cintiq 13HD touch Pen",
	product_id = 0x0333,
	reports = (
		set_mode_intuos3,
		device_id_report_cintiq13,
		generic_stylus_intuos4,
		airbrush_report_inutos4,
		artpen_report_intuos4,
		express_keys_cintiq_13HD,
	),
	logical_mins = {
		"X": 400,
		"Y": 400,
		"Twist": -900,
	},
	logical_maxs = {
		"X": 59152,
		"Y": 33448,
		"Twist": 899,
		"Wheel": 1023,
		"Tip Pressure": 2047,
		"Altitude": 63,
		"X Tilt": 127,
		"Y Tilt": 127,
	},
	physical_mins = {
		"X Tilt": -64,
		"Y Tilt": -64,
	},
	physical_maxs = {
		"X": 2940,
		"Y": 1650,
		"Twist": 359,
		"X Tilt": 63,
		"Y Tilt": 63,
	},
	original_reports = "228 05 01 09 02 a1 01 85 01 09 01 a1 00 05 09 19 01 29 03 15 00 25 01 95 03 75 01 81 02 95 05 81 03 05 01 09 30 09 31 09 38 15 81 25 7f 75 08 95 03 81 06 c0 c0 06 0d ff 09 01 a1 01 85 10 09 00 75 08 96 09 00 15 00 26 ff 00 81 02 85 11 09 00 75 08 96 09 00 15 00 26 ff 00 81 02 85 c0 09 00 75 08 96 09 00 15 00 26 ff 00 81 02 85 02 09 00 95 01 b1 02 85 03 09 00 95 01 b1 02 85 05 09 00 95 08 b1 02 85 07 09 00 95 0f b1 02 85 08 09 00 95 04 b1 02 85 0a 09 00 95 02 b1 02 85 0b 09 00 95 01 b1 02 85 04 09 00 95 01 b1 02 85 0d 09 00 95 01 b1 02 85 0f 09 00 95 07 b1 02 85 10 09 00 95 03 b1 02 85 30 09 00 95 01 b1 02 85 cc 09 00 95 02 b1 02 85 40 09 00 95 02 b1 02 85 dd 09 00 95 01 b1 02 c0",
	sibling_device = (0x056a, 0x335),
)

cintiq_13HDT_touch = Wacom(
	name = "Wacom Cintiq 13HD touch Finger",
	product_id = 0x0335,
	original_reports = "555 05 0d 09 04 a1 01 85 01 09 22 a1 02 09 42 15 00 25 01 75 01 95 01 81 02 81 03 81 03 95 05 81 03 75 08 09 51 95 01 81 02 05 01 75 10 95 02 55 0e 65 11 09 30 26 79 0b 35 00 46 79 0b 81 02 46 74 06 09 31 26 74 06 81 02 05 0d 95 01 09 48 81 02 09 49 81 02 c0 05 0d 09 22 a1 02 09 42 15 00 25 01 75 01 95 01 81 02 81 03 81 03 95 05 81 03 75 08 09 51 95 01 81 02 05 01 75 10 95 02 55 0e 65 11 09 30 26 79 0b 35 00 46 79 0b 81 02 46 74 06 09 31 26 74 06 81 02 05 0d 95 01 09 48 81 02 09 49 81 02 c0 05 0d 09 22 a1 02 09 42 15 00 25 01 75 01 95 01 81 02 81 03 81 03 95 05 81 03 75 08 09 51 95 01 81 02 05 01 75 10 95 02 55 0e 65 11 09 30 26 79 0b 35 00 46 79 0b 81 02 46 74 06 09 31 26 74 06 81 02 05 0d 95 01 09 48 81 02 09 49 81 02 c0 05 0d 09 22 a1 02 09 42 15 00 25 01 75 01 95 01 81 02 81 03 81 03 95 05 81 03 75 08 09 51 95 01 81 02 05 01 75 10 95 02 55 0e 65 11 09 30 26 79 0b 35 00 46 79 0b 81 02 46 74 06 09 31 26 74 06 81 02 05 0d 95 01 09 48 81 02 09 49 81 02 c0 05 0d 27 ff ff ff 0f 75 20 95 01 09 56 81 02 09 54 26 ff 00 95 01 75 08 81 02 85 10 09 55 95 02 25 0a b1 02 85 11 06 00 ff 09 c5 96 00 01 b1 02 c0 05 0d 09 0e a1 01 85 12 09 23 a1 02 09 52 09 53 15 00 25 0a 75 08 95 02 b1 02 c0 c0 05 0d 09 04 a1 01 85 02 09 22 a1 02 09 42 15 00 25 01 75 01 95 01 81 02 95 07 81 03 05 01 75 10 95 01 55 0e 65 11 09 30 26 79 0b 35 00 46 79 0b 81 02 46 74 06 09 31 26 74 06 81 02 c0 05 0d 09 56 27 ff ff ff 0f 75 20 95 01 81 02 09 54 26 ff 00 95 01 75 08 81 02 c0 05 01 09 02 a1 01 85 03 09 01 a1 00 05 09 19 01 29 02 15 00 25 01 95 02 75 01 81 02 95 01 75 06 81 03 05 01 75 10 95 01 55 0e 65 11 09 30 26 79 0b 35 00 46 79 0b 81 02 46 74 06 09 31 26 74 06 81 02 c0 c0",
	reports = (
		[int(i, 16) for i in "05 0d 09 04 a1 01 85 01 09 22 a1 02 09 42 15 00 25 01 75 01 95 01 81 02 81 03 81 03 95 05 81 03 75 08 09 51 95 01 81 02 05 01 75 10 95 02 55 0e 65 11 09 30 26 79 0b 35 00 46 79 0b 81 02 46 74 06 09 31 26 74 06 81 02 05 0d 95 01 09 48 81 02 09 49 81 02 c0 05 0d 09 22 a1 02 09 42 15 00 25 01 75 01 95 01 81 02 81 03 81 03 95 05 81 03 75 08 09 51 95 01 81 02 05 01 75 10 95 02 55 0e 65 11 09 30 26 79 0b 35 00 46 79 0b 81 02 46 74 06 09 31 26 74 06 81 02 05 0d 95 01 09 48 81 02 09 49 81 02 c0 05 0d 09 22 a1 02 09 42 15 00 25 01 75 01 95 01 81 02 81 03 81 03 95 05 81 03 75 08 09 51 95 01 81 02 05 01 75 10 95 02 55 0e 65 11 09 30 26 79 0b 35 00 46 79 0b 81 02 46 74 06 09 31 26 74 06 81 02 05 0d 95 01 09 48 81 02 09 49 81 02 c0 05 0d 09 22 a1 02 09 42 15 00 25 01 75 01 95 01 81 02 81 03 81 03 95 05 81 03 75 08 09 51 95 01 81 02 05 01 75 10 95 02 55 0e 65 11 09 30 26 79 0b 35 00 46 79 0b 81 02 46 74 06 09 31 26 74 06 81 02 05 0d 95 01 09 48 81 02 09 49 81 02 c0 05 0d 27 ff ff ff 0f 75 20 95 01 09 56 81 02 09 54 26 ff 00 95 01 75 08 81 02 85 10 09 55 95 02 25 0a b1 02 85 11 06 00 ff 09 c5 96 00 01 b1 02 c0 05 0d 09 0e a1 01 85 12 09 23 a1 02 09 52 09 53 15 00 25 0a 75 08 95 02 b1 02 c0 c0 05 0d 09 04 a1 01 85 02 09 22 a1 02 09 42 15 00 25 01 75 01 95 01 81 02 95 07 81 03 05 01 75 10 95 01 55 0e 65 11 09 30 26 79 0b 35 00 46 79 0b 81 02 46 74 06 09 31 26 74 06 81 02 c0 05 0d 09 56 27 ff ff ff 0f 75 20 95 01 81 02 09 54 26 ff 00 95 01 75 08 81 02 c0 05 01 09 02 a1 01 85 03 09 01 a1 00 05 09 19 01 29 02 15 00 25 01 95 02 75 01 81 02 95 01 75 06 81 03 05 01 75 10 95 01 55 0e 65 11 09 30 26 79 0b 35 00 46 79 0b 81 02 46 74 06 09 31 26 74 06 81 02 c0 c0".split()],
	),
	sibling_device = (0x056a, 0x333),
	logical_mins = {
	},
	logical_maxs = {
	},
	physical_mins = {
	},
	physical_maxs = {
	},
)
