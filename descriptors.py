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

boot_mouse_collection = (
	0x05, 0x01,			# Usage Page (Generic Desktop)
	0x09, 0x01,			# Usage (Pointer)
	0xa1, 0x01,			# Collection (Application)
	0x85, 0x01,			#  Report ID (1)
	0x09, 0x01,			#  Usage (Pointer)
	0xa1, 0x00,			#  Collection (Physical)
	0x05, 0x09,			#   Usage Page (Button)
	0x19, 0x01,			#   Usage Minimum (1)
	0x29, 0x03,			#   Usage Maximum (3)
	0x15, 0x00,			#   Logical Minimum (0)
	0x25, 0x01,			#   Logical Maximum (1)
	0x95, 0x03,			#   Report Count (3)
	0x75, 0x01,			#   Report Size (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x95, 0x05,			#   Report Count (5)
	0x81, 0x03,			#   Input (Cnst,Var,Abs)
	0x05, 0x01,			#   Usage Page (Generic Desktop)
	0x09, 0x30,			#   Usage (X)
	0x09, 0x31,			#   Usage (Y)
	0x09, 0x38,			#   Usage (Wheel)
	0x15, 0x81,			#   Logical Minimum (-127)
	0x25, 0x7f,			#   Logical Maximum (127)
	0x75, 0x08,			#   Report Size (8)
	0x95, 0x03,			#   Report Count (3)
	0x81, 0x06,			#   Input (Data,Var,Rel)
	0xc0,				#  End Collection
	0xc0,				# End Collection
)

device_id_report_intuos3 = (
	0x05, 0x0d,			# Usage Page (Digitizers)
	0x09, 0x02,			# Usage (Pen)
	0xa1, 0x01,			# Collection (Application)
	0x85, 0x02,			#  Report ID (2)

	0x09, 0x01,			#  Usage (Digitizer)
	0xa1, 0x00,			#  Collection (Physical)

	0x05, 0xbe,			#   Usage Page (Wacom Custom)
	0x09, 0x05,			#   Usage (Intuos Sub Report ID)
	0x75, 0x06,			#   Report Size (6)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x05, 0x0d,			#   Usage Page (Digitizers)
	0x09, 0x32,			#   Usage (In Range)
	0x75, 0x01,			#   Report Size (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0x06, 0x0d, 0xbe,		#   Usage Page (Digitizers + offset)
	0x0a, 0x38, 0x04,		#   Usage (Transducer Index << 4)
	0x75, 0x08,			#   Report Size (8)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x0a, 0x5b, 0x1c,		#   Usage (Transducer Serial Number << 28)
	0x75, 0x04,			#   Report Size (4)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x0a, 0x38, 0x00,		#   Usage (Transducer Index << 0)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x0a, 0x5b, 0x14,		#   Usage (Transducer Serial Number << 20)
	0x75, 0x08,			#   Report Size (8)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x0a, 0x5b, 0x0c,		#   Usage (Transducer Serial Number << 12)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x0a, 0x5b, 0x04,		#   Usage (Transducer Serial Number << 4)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x0a, 0x38, 0x14,		#   Usage (Transducer Index << 20)
	0x75, 0x04,			#   Report Size (4)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x0a, 0x5b, 0x00,		#   Usage (Transducer Serial Number << 0)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x75, 0x08,			#   Report Size (8)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0x75, 0x04,			#   Report Size (4)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0x0a, 0x38, 0x0c,		#   Usage (Transducer Index << 12)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x05, 0x0d,			#   Usage Page (Digitizers)
	0x09, 0x52,			#   Usage (Inputmode)
	0x95, 0x01,			#   Report Count (1)
	0xb1, 0x02,			#   Feature (Data,Var,Abs)

	0xc0,				#  End Collection
	0xc0,				# End Collection
)

generic_stylus_intuos4 = (
	0x05, 0x0d,			# Usage Page (Digitizers)
	0x09, 0x02,			# Usage (Pen)
	0xa1, 0x01,			# Collection (Application)
	0x85, 0x04,			#  Report ID (4)

	0x09, 0x20,			#  Usage (Stylus)
	0xa1, 0x00,			#  Collection (Physical)

	0x06, 0x0d, 0xbe,		#   Usage Page (Digitizers + offset)
	0x0a, 0x30, 0x00,		#   Usage (Tip Pressure << 0)
	0x75, 0x01,			#   Report Size (1)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x05, 0x09,			#   Usage Page (Button)
	0x09, 0x4b,			#   Usage (Vendor Usage 0x4b)
	0x09, 0x4c,			#   Usage (Vendor Usage 0x4c)
	0x95, 0x02,			#   Report Count (2)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x05, 0xbe,			#   Usage Page (Wacom Custom)
	0x09, 0x05,			#   Usage (Intuos Sub Report ID)
	0x75, 0x03,			#   Report Size (3)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x05, 0x0d,			#   Usage Page (Digitizers)
	0x09, 0x32,			#   Usage (In Range)
	0x75, 0x01,			#   Report Size (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x06, 0x00, 0xff,		#   Usage Page (Vendor Defined Page 1)
	0x09, 0x00,			#   Usage (Undefined)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0x06, 0x01, 0xbe,		#   Usage Page (Generic Desktop + offset
	0x0a, 0x30, 0x09,		#   Usage (X << 9)
	0x0a, 0x30, 0x01,		#   Usage (X << 1)
	0x75, 0x08,			#   Report Size (8)
	0x95, 0x02,			#   Report Count (2)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x0a, 0x31, 0x09,		#   Usage (Y << 9)
	0x0a, 0x31, 0x01,		#   Usage (Y << 1)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x06, 0x0d, 0xbe,		#   Usage Page (Digitizers + offset)
	0x0a, 0x30, 0x03,		#   Usage (Tip Pressure << 3)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x0a, 0x3d, 0x01,		#   Usage (X Tilt << 1)
	0x75, 0x06,			#   Report Size (6)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x06, 0x0d, 0xbe,		#   Usage Page (Digitizers + offset)
	0x0a, 0x30, 0x01,		#   Usage (Tip Pressure << 1)
	0x75, 0x02,			#   Report Size (2)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x05, 0x0d,			#   Usage Page (Digitizers)
	0x09, 0x3e,			#   Usage (Y Tilt)
	0x75, 0x07,			#   Report Size (7)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x06, 0x0d, 0xbe,		#   Usage Page (Digitizers + offset)
	0x09, 0x3d,			#   Usage (X Tilt << 0)
	0x75, 0x01,			#   Report Size (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x06, 0x01, 0xbe,		#   Usage Page (Generic Desktop + offset
	0x09, 0x31,			#   Usage (Y << 0)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x09, 0x30,			#   Usage (X << 0)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x05, 0x0d,			#   Usage Page (Digitizers)
	0x09, 0x40,			#   Usage (Altitude)
	0x75, 0x06,			#   Report Size (6)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0xc0,				#  End Collection
	0xc0,				# End Collection
)

airbrush_report_inutos4 = (
	0x05, 0x0d,			# Usage Page (Digitizers)
	0x09, 0x02,			# Usage (Pen)
	0xa1, 0x01,			# Collection (Application)

	0x85, 0x34,			#  Report ID (52)
	0x09, 0x20,			#  Usage (Stylus)
	0xa1, 0x00,			#  Collection (Physical)

	0x06, 0x01, 0xbe,		#   Usage Page (Generic Desktop + offset)
	0x05, 0xbe,			#   Usage Page (Wacom Custom)
	0x09, 0x05,			#   Usage (Intuos Sub Report ID)
	0x75, 0x06,			#   Report Size (6)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x05, 0x0d,			#   Usage Page (Digitizers)
	0x09, 0x32,			#   Usage (In Range)
	0x75, 0x01,			#   Report Size (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x06, 0x00, 0xff,		#   Usage Page (Vendor Defined Page 1)
	0x09, 0x00,			#   Usage (Undefined)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0x06, 0x01, 0xbe,		#   Usage Page (Generic Desktop + offset)
	0x0a, 0x30, 0x09,		#   Usage (X << 9)
	0x0a, 0x30, 0x01,		#   Usage (X << 1)
	0x75, 0x08,			#   Report Size (8)
	0x95, 0x02,			#   Report Count (2)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x0a, 0x31, 0x09,		#   Usage (Y << 9)
	0x0a, 0x31, 0x01,		#   Usage (Y << 1)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x0a, 0x38, 0x02,		#   Usage (Wheel << 2)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x06, 0x0d, 0xbe,		#   Usage Page (Digitizers + offset)
	0x0a, 0x3d, 0x01,		#   Usage (X Tilt << 1)
	0x75, 0x06,			#   Report Size (6)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x06, 0x01, 0xbe,		#   Usage Page (Generic Desktop + offset)
	0x0a, 0x38, 0x00,		#   Usage (Wheel << 0)
	0x75, 0x02,			#   Report Size (2)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x05, 0x0d,			#   Usage Page (Digitizers)
	0x09, 0x3e,			#   Usage (Y Tilt)
	0x75, 0x07,			#   Report Size (7)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x06, 0x0d, 0xbe,		#   Usage Page (Digitizers + offset)
	0x09, 0x3d,			#   Usage (X Tilt << 0)
	0x75, 0x01,			#   Report Size (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x06, 0x01, 0xbe,		#   Usage Page (Generic Desktop + offset)
	0x09, 0x31,			#   Usage (Y << 0)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x09, 0x30,			#   Usage (X << 0)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x05, 0x0d,			#   Usage Page (Digitizers)
	0x09, 0x40,			#   Usage (Altitude)
	0x75, 0x06,			#   Report Size (6)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0xc0,				#  End Collection
	0xc0,				# End Collection
)

five_button_mouse_report_intuos4 = (
	0x05, 0x0d,			# Usage Page (Digitizers)
	0x09, 0x02,			# Usage (Pen)
	0xa1, 0x01,			# Collection (Application)

	0x85, 0x2c,			#  Report ID (44)

	0x05, 0x01,			# Usage Page (Generic Desktop)
	0x09, 0x02,			#  Usage (Mouse)
	0xa1, 0x00,			#  Collection (Physical)

	0x05, 0xbe,			#   Usage Page (Wacom Custom)
	0x09, 0x05,			#   Usage (Intuos Sub Report ID)
	0x75, 0x06,			#   Report Size (6)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x05, 0x0d,			#   Usage Page (Digitizers)
	0x09, 0x32,			#   Usage (In Range)
	0x75, 0x01,			#   Report Size (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0x06, 0x01, 0xbe,		#   Usage Page (Generic Desktop + offset)
	0x0a, 0x30, 0x09,		#   Usage (X << 9)
	0x0a, 0x30, 0x01,		#   Usage (X << 1)
	0x75, 0x08,			#   Report Size (8)
	0x95, 0x02,			#   Report Count (2)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x0a, 0x31, 0x09,		#   Usage (Y << 9)
	0x0a, 0x31, 0x01,		#   Usage (Y << 1)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x05, 0x09,			#   Usage Page (Button)
	0x09, 0x10,			#   Usage (Vendor Usage 0x10)
	0x09, 0x12,			#   Usage (Vendor Usage 0x12)
	0x09, 0x11,			#   Usage (Vendor Usage 0x11)
	0x09, 0x13,			#   Usage (Vendor Usage 0x13)
	0x09, 0x14,			#   Usage (Vendor Usage 0x14)
	0x75, 0x01,			#   Report Size (1)
	0x95, 0x05,			#   Report Count (5)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x75, 0x03,			#   Report Size (3)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0x06, 0x0d, 0xbe,		#   Usage Page (Digitizers + offset)
	0x0a, 0x3d, 0x01,		#   Usage (X Tilt << 1)
	0x75, 0x06,			#   Report Size (6)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x05, 0x01,			#   Usage Page (Generic Desktop)
	0x09, 0x38,			#   Usage (Wheel)
	0x15, 0xff,			#   Logical Minimum (-1)
	0x25, 0x01,			#   Logical Maximum (1)
	0x75, 0x02,			#   Report Size (2)
	0x81, 0x06,			#   Input (Data,Var,Rel)

	0x06, 0x0d, 0xbe,		#   Usage Page (Digitizers + offset)
	0x0a, 0x3e, 0x00,		#   Usage (Y Tilt << 0)
	0x75, 0x07,			#   Report Size (7)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x0a, 0x3d, 0x01,		#   Usage (X Tilt << 1)
	0x75, 0x01,			#   Report Size (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x06, 0x01, 0xbe,		#   Usage Page (Generic Desktop + offset)
	0x09, 0x31,			#   Usage (Y << 0)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x09, 0x30,			#   Usage (X << 0)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x05, 0x0d,			#   Usage Page (Digitizers)
	0x09, 0x40,			#   Usage (Altitude)
	0x75, 0x06,			#   Report Size (6)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0xc0,				#  End Collection
	0xc0,				# End Collection
)

artpen_report_intuos4 = (
	0x05, 0x0d,			# Usage Page (Digitizers)
	0x09, 0x02,			# Usage (Pen)
	0xa1, 0x01,			# Collection (Application)

	0x85, 0x2a,			#  Report ID (42)
	0x09, 0x20,			#  Usage (Stylus)
	0xa1, 0x00,			#  Collection (Physical)

	0x05, 0xbe,			#   Usage Page (Wacom Custom)
	0x09, 0x05,			#   Usage (Intuos Sub Report ID)
	0x75, 0x06,			#   Report Size (6)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x05, 0x0d,			#   Usage Page (Digitizers)
	0x09, 0x32,			#   Usage (In Range)
	0x75, 0x01,			#   Report Size (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0x06, 0x01, 0xbe,		#   Usage Page (Generic Desktop + offset)
	0x0a, 0x30, 0x09,		#   Usage (X << 9)
	0x0a, 0x30, 0x01,		#   Usage (X << 1)
	0x75, 0x08,			#   Report Size (8)
	0x95, 0x02,			#   Report Count (2)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x0a, 0x31, 0x09,		#   Usage (Y << 9)
	0x0a, 0x31, 0x01,		#   Usage (Y << 1)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x06, 0x0d, 0xbe,		#   Usage Page (Digitizers + offset)
	0x0a, 0x41, 0x03,		#   Usage (Twist << 3)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x75, 0x05,			#   Report Size (5)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)
	0x0a, 0x41, 0x00,		#   Usage (Twist << 0)
	0x75, 0x03,			#   Report Size (3)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x75, 0x08,			#   Report Size (8)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0x06, 0x01, 0xbe,		#   Usage Page (Generic Desktop + offset)
	0x09, 0x31,			#   Usage (Y << 0)
	0x75, 0x01,			#   Report Size (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x09, 0x30,			#   Usage (X << 0)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x05, 0x0d,			#   Usage Page (Digitizers)
	0x09, 0x40,			#   Usage (Altitude)
	0x75, 0x06,			#   Report Size (6)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0xc0,				#  End Collection
	0xc0,				# End Collection
)

tablet_buttons_report_intuos4 = (
	0x05, 0x01,			# Usage Page (Generic Desktop)
	0x09, 0x02,			# Usage (Pen)
	0xa1, 0x01,			# Collection (Application)

	0x85, 0x0c,			#  Report ID (12)
	0x09, 0x07,			#  Usage (Keypad)
	0xa1, 0x00,			#  Collection (Physical)

	0x05, 0x01,			#   Usage Page (Generic Desktop)
	0x09, 0x38,			#   Usage (Wheel)
	0x75, 0x07,			#   Report Size (7)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x05, 0x09,			#   Usage Page (Button)
	0x09, 0x20,			#   Usage (Vendor Usage 0x20)
	0x75, 0x01,			#   Report Size (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x09, 0x00,			#   Usage (No Buttons Pressed)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x95, 0x07,			#   Report Count (7)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0x95, 0x08,			#   Report Count (8)
	0x19, 0x01,			#   Usage Minimum (1)
	0x29, 0x08,			#   Usage Maximum (8)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x95, 0x30,			#   Report Count (48)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0xc0,				#  End Collection
	0xc0,				# End Collection
)

express_keys_touch_ring_intuos5 = (
	0x05, 0x01,			# Usage Page (Generic Desktop)
	0x09, 0x02,			# Usage (Pen)
	0xa1, 0x01,			# Collection (Application)

	0x85, 0x03,			#  Report ID (3)
	0x09, 0x07,			#  Usage (Keypad)
	0xa1, 0x00,			#  Collection (Physical)

	0x75, 0x08,			#   Report Size (8)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0x05, 0x01,			#   Usage Page (Generic Desktop)
	0x09, 0x38,			#   Usage (Wheel)
	0x75, 0x07,			#   Report Size (7)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x05, 0x09,			#   Usage Page (Button)
	0x09, 0x20,			#   Usage (Vendor Usage 0x20)
	0x75, 0x01,			#   Report Size (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x09, 0x00,			#   Usage (No Buttons Pressed)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x95, 0x07,			#   Report Count (7)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0x95, 0x08,			#   Report Count (8)
	0x19, 0x01,			#   Usage Minimum (1)
	0x29, 0x08,			#   Usage Maximum (8)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x19, 0x09,			#   Usage Minimum (9)
	0x29, 0x10,			#   Usage Maximum (16)
	0x81, 0x01,			#   Input (Data,Var,Abs)

	0x95, 0x14,			#   Report Count (20)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0xc0,				#  End Collection
	0xc0,				# End Collection
)

express_keys_touch_ring_intuos5_s = (
	0x05, 0x01,			# Usage Page (Generic Desktop)
	0x09, 0x07,			# Usage (Keypad)
	0xa1, 0x01,			# Collection (Application)

	0x85, 0x03,			#  Report ID (3)
	0x09, 0x07,			#  Usage (Keypad)
	0xa1, 0x00,			#  Collection (Physical)

	0x75, 0x08,			#   Report Size (8)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0x05, 0x01,			#   Usage Page (Generic Desktop)
	0x09, 0x38,			#   Usage (Wheel)
	0x75, 0x07,			#   Report Size (7)
	0x95, 0x01,			#   Report Count (1)
	0x15, 0x00,			#   Logical Minimum (0)
	0x25, 0x47,			#   Logical Maximum (71)

	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x05, 0xbe,			#   Usage Page (Wacom Custom)
	0x09, 0x20,			#   Usage (Vendor Usage 0x20)
	0x75, 0x01,			#   Report Size (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x05, 0x09,			#   Usage Page (Button)
	0x09, 0x00,			#   Usage (No Buttons Pressed)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x95, 0x07,			#   Report Count (7)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0x95, 0x06,			#   Report Count (6)
	0x19, 0x01,			#   Usage Minimum (1)
	0x29, 0x06,			#   Usage Maximum (6)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x95, 0x02,			#   Report Count (2)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

#	0x19, 0x09,			#   Usage Minimum (9)
#	0x29, 0x0e,			#   Usage Maximum (14)
#	0x95, 0x06,			#   Report Count (6)
#	0x81, 0x01,			#   Input (Data,Var,Abs)

	0x95, 0x1c,			#   Report Count (28)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0xc0,				#  End Collection
	0xc0,				# End Collection
)

express_keys_touch_strip_cintiq_22HD = (
	0x05, 0x01,			# Usage Page (Generic Desktop)
	0x09, 0x02,			# Usage (Pen)
	0xa1, 0x01,			# Collection (Application)

	0x85, 0x0c,			#  Report ID (12)
	0x09, 0x07,			#  Usage (Keypad)
	0xa1, 0x00,			#  Collection (Physical)

	0x06, 0x01, 0xbe,		#   Usage Page (Generic Desktop + offset)
	0x0a, 0x33, 0x08,		#   Usage (Rx << 8)
	0x09, 0x33,			#   Usage (Rx << 0)
	0x75, 0x08,			#   Report Size (8)
	0x96, 0x02, 0x00,		#   Report Count (2)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x0a, 0x34, 0x08,		#   Usage (Ry << 8)
	0x09, 0x34,			#   Usage (Ry << 0)
	0x75, 0x08,			#   Report Size (8)
	0x96, 0x02, 0x00,		#   Report Count (2)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x05, 0x09,			#   Usage Page (Button)
	0x75, 0x01,			#   Report Size (1)
	0x95, 0x01,			#   Report Count (1)
	0x09, 0x00,			#   Usage (No Buttons Pressed)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x75, 0x01,			#   Report Size (1)
	0x95, 0x07,			#   Report Count (7)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0x95, 0x08,			#   Report Count (8)
	0x19, 0x01,			#   Usage Minimum (1)
	0x29, 0x08,			#   Usage Maximum (8)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x09, 0x09,			#   Usage (Vendor Usage 0x09)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x95, 0x07,			#   Report Count (7)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0x09, 0x30,			#   Usage (Vendor Usage 0x30)
	0x09, 0x31,			#   Usage (Vendor Usage 0x31)
	0x09, 0x32,			#   Usage (Vendor Usage 0x32)
	0x09, 0x33,			#   Usage (Vendor Usage 0x33)
	0x09, 0x34,			#   Usage (Vendor Usage 0x34)
	0x09, 0x35,			#   Usage (Vendor Usage 0x35)
	0x09, 0x26,			#   Usage (Vendor Usage 0x26)
	0x09, 0x27,			#   Usage (Vendor Usage 0x27)
	0x95, 0x08,			#   Report Count (8)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x05, 0x07,			#   Usage Page (Keyboard)
	0x09, 0x94,			#   Usage (LANG5)
	0x09, 0x95,			#   Usage (LANG6)
	0x09, 0xca,			#   Usage (Vendor Usage 0xca)
	0x95, 0x03,			#   Report Count (3)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x06, 0x09, 0xbe,		#   Usage Page (Button + offset)
	0x0a, 0x4b, 0x01,		#   Usage (Vendor Usage 0x14b)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x95, 0x04,			#   Report Count (4)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0xc0,				#  End Collection
	0xc0,				# End Collection
)

express_keys_touch_ring_cintiq_24HD = (
	0x05, 0x01,			# Usage Page (Generic Desktop)
	0x09, 0x02,			# Usage (Pen)
	0xa1, 0x01,			# Collection (Application)

	0x85, 0x0c,			#  Report ID (12)
	0x09, 0x07,			#  Usage (Keypad)
	0xa1, 0x00,			#  Collection (Physical)

	0x05, 0x01,			#   Usage Page (Generic Desktop)
	0x09, 0x38,			#   Usage (Wheel)
	0x75, 0x07,			#   Report Size (7)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x05, 0x09,			#   Usage Page (Button)
	0x09, 0x20,			#   Usage (Vendor Usage 0x20)
	0x75, 0x01,			#   Report Size (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x05, 0x01,			#   Usage Page (Generic Desktop)
	0x09, 0x38,			#   Usage (Wheel)
	0x75, 0x07,			#   Report Size (7)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
	0x05, 0x09,			#   Usage Page (Button)
	0x09, 0x20,			#   Usage (Vendor Usage 0x20)
	0x75, 0x01,			#   Report Size (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x06, 0x01, 0xbe,		#   Usage Page (Generic Desktop + offset)
	0x0a, 0x33, 0x08,		#   Usage (Rx << 8)
	0x09, 0x33,			#   Usage (Rx << 0)
	0x75, 0x08,			#   Report Size (8)
	0x96, 0x02, 0x00,		#   Report Count (2)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x75, 0x01,			#   Report Size (1)
	0x95, 0x08,			#   Report Count (8)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0x05, 0x09,			#   Usage Page (Button)
	0x19, 0x00,			#   Usage Minimum (0)
	0x29, 0x07,			#   Usage Maximum (7)
	0x95, 0x08,			#   Report Count (8)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x75, 0x01,			#   Report Size (1)
	0x95, 0x08,			#   Report Count (8)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0x19, 0x08,			#   Usage Minimum (8)
	0x29, 0x0f,			#   Usage Maximum (15)
	0x81, 0x02,			#   Input (Data,Var,Abs)

	0x75, 0x01,			#   Report Size (1)
	0x95, 0x08,			#   Report Count (8)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)

	0xc0,				#  End Collection
	0xc0,				# End Collection
)

led_configuration_intuos5 = (
	0x05, 0x01,			# Usage Page (Generic Desktop)
	0x09, 0x07,			# Usage (Keypad)
	0xa1, 0x01,			# Collection (Application)

	0x85, 0x20,			#  Report ID (32)
	0xa1, 0x00,			#  Collection (Physical)

	0x05, 0xbe,			#   Usage Page (Wacom Custom)
	0x09, 0x07,			#   Usage (LED Select ID)
	0x09, 0x08,			#   Usage (Indicator LED Brightness)
	0x09, 0x0b,			#   Usage (LED Crop Mark Brightness)
	0x75, 0x06,			#   Report Size (2)
	0x95, 0x01,			#   Report Count (3)
	0xb1, 0x02,			#   Feature (Data,Var,Abs)

	0x75, 0x3a,			#   Report Size (58)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x03,			#   Feature (Cnst,Arr,Abs)

	0xc0,				#  End Collection
	0xc0,				# End Collection
)

bpt3_touch_msg_header = (
	0x05, 0x0d,			# Usage Page (Digitizers)
	0x09, 0x05,			# Usage (Touch Pad)
	0xa1, 0x01,			# Collection (Application)
	0x85, 0x02,			#  Report ID (2)
	0x09, 0x22,			#  Usage (Finger)
	0xa1, 0x02,			#  Collection (Logical)
	0x05, 0x0d,			#   Usage Page (Digitizers)
	0x09, 0x54,			#   Usage (Contact Count)
	0x15, 0x00,			#   Logical Minimum (0)
	0x25, 0x0f,			#   Logical Maximum (15)
	0x75, 0x08,			#   Report Size (8)
	0x95, 0x01,			#   Report Count (1)
	0x81, 0x02,			#   Input (Data,Var,Abs)
)

bpt3_touch_msg_finger = (
	0xa1, 0x02,			#   Collection (Logical)
	0x05, 0x0d,			#    Usage Page (Digitizers)
	0x09, 0x51,			#    Usage (Contact Id)
	0x15, 0x02,			#    Logical Minimum (2)
	0x25, 0x11,			#    Logical Maximum (17)
	0x75, 0x08,			#    Report Size (8)
	0x95, 0x01,			#    Report Count (1)
	0x81, 0x02,			#    Input (Data,Var,Abs)

	0x75, 0x01,			#    Report Size (1)
	0x05, 0xff,			#    Usage Page (Vendor Usage Page 0xff)
	0x75, 0x07,			#    Report Size (7)
	0x81, 0x01,			#    Input (Cnst,Arr,Abs)

	0x05, 0x0d,			#    Usage Page (Digitizers)
	0x09, 0x42,			#    Usage (Tip Switch)
	0x15, 0x00,			#    Logical Minimum (0)
	0x25, 0x01,			#    Logical Maximum (1)
	0x75, 0x01,			#    Report Size (1)
	0x81, 0x02,			#    Input (Data,Var,Abs)

	0x06, 0x01, 0xbe,		#    Usage Page (Generic Desktop + offset)
	0x55, 0x0f,			#    Unit Exponent (-1)
	0x65, 0x11,			#    Unit (Centimeter,SILinear)
	0x0a, 0x30, 0x04,		#    Usage (X << 4)
	0x75, 0x08,			#    Report Size (8)
	0x95, 0x01,			#    Report Count (1)
	0x81, 0x02,			#    Input (Data,Var,Abs)

	0x0a, 0x31, 0x04,		#    Usage (Y << 4)
	0x81, 0x02,			#    Input (Data,Var,Abs)

	0x09, 0x30,			#    Usage (X << 0)
	0x75, 0x04,			#    Report Size (4)
	0x95, 0x01,			#    Report Count (1)
	0x81, 0x02,			#    Input (Data,Var,Abs)

	0x09, 0x31,			#    Usage (Y << 0)
	0x81, 0x02,			#    Input (Data,Var,Abs)

	0x06, 0x0d, 0xbe,		#    Usage Page (Digitizers + offset)
	0x0a, 0x48, 0x07,		#    Usage (Width << 7)
	0x0a, 0x49, 0x07,		#    Usage (Height << 7)
	0x75, 0x08,			#    Report Size (8)
	0x95, 0x02,			#    Report Count (2)
	0x81, 0x02,			#    Input (Data,Var,Abs)

	0x05, 0xff,			#    Usage Page (Vendor Usage Page 0xff)
	0x75, 0x08,			#    Report Size (8)
	0x95, 0x01,			#    Report Count (1)
	0x81, 0x01,			#    Input (Cnst,Arr,Abs)
	0xc0,				#   End Collection
)

bpt3_touch_msg_footer = (
	0x75, 0x08,			#   Report Size (8)
	0x95, 0x06,			#   Report Count (6)
	0x81, 0x01,			#   Input (Cnst,Arr,Abs)
	0xc0,				#  End Collection
	0xc0,				# End Collection
)
