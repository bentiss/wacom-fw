# wacom-fw
Custom writing of Wacom firmwares

# What is is?
This is an experimental playground with Wacom devices.

# Why this work is done?
I am very glad that Wacom (the company) invested so much time and effort in the Linux Wacom project.
However, given the amount of devices they support, the wacom.ko driver has become bigger and bigger, and just looks like
a giant spaghetti plate.

The proposal here is to externalize the description of the wacom devices and their protocols.
By forging custom report descriptors and firmware information, we are able to provide to the kernel the rosetta stone
it needs to understand what the tablet output in its USB events. This should allow us to stop the growth of the driver
in the kernel. 
The other net benefit will be that the support of a new device will be just adding a file in the
firmware directory, which is painless for distributions and users. Distributions will have to update the firmware package
and users which distribution will not have the correct firmware will just need to grab the firmware and put it in their local
filesystem.

# How to run the tool
This tool should be run once, and you should forget about it.
The firmwares will eventually be shipped by the distributions, so there will be no need to run it at all
except for adding new devices.

Grab this tree, and run the following commands to initialize the hid-replay submodule:
```bash
#> git submodule init
#> git submodule update
```

The entry point is `create_wacom_firmwares.py` and if you just run it with python (2.x IIRC),
it will create the requested firmwares in the `output/` subdirectory

# What does the tool produces?
The tools outputs 2 types of files in the `output` subdirectory (each XXX is a different PID):
- 0003_056a_XXXX.bin: this is the actual binary that will be loaded by the kernel eventually
- 0003_056a_XXXX.hid: this is a text file that can be understood by the hid-replay tools

You can have a better look at the produced report descriptor by calling (at the root of this tree):
```bash
#> python hid-replay/tools/parse_rdesc.py output/0003_056a_XXX.hid
```

# OK, how do I play with it?
You need quite a little setup before being able to use those firmwares:
- a lot of good faith and luck
- be sure that your tablet is supported
- a kernel which wacom.ko module supports loading external firmwares:
  - [this tree](https://github.com/bentiss/linux) contains an experimental branch, named something like hid-wacom-###.
  - grab the latest branch
  - remove the support of your tablet: comment out it's PIDs in wacom_ids[] in drivers/hid/wacom_wac.c
  - compile it
  - install it
  - reboot

Then, copy all the firmwares (the *.bin in output) in /lib/firmwares/hid (you need to create this directory first).

You need to unplug/replug the tablet, and hopefully the kernel will fetch the firmware(s) and the tablet should work as before :)

# Which License?
Currently GPL v2, and so are the produced firmwares.
I wrote all the code and various report descriptors used here, so I am fine putting this work under GPL v2.

# Is there an ETA when this work will get upstream?
No.

There are a lot of issues to fix first (see the TODO file).
We also want to have features parity with existing devices before being able to submit this work (there should be no
differences either you are using a custom firmware produced here or when the device was registered in wacom.ko).
Last, we are loading external binaries in the kernel space, so we need to be solid rock regarding the firmwares, and this might
take some time to assess that there is no problems.

Then, when we will be happy with that, there is always the chance this gets rejected upstream (most
of the time for good reasons). So no ETA.

# Psst, the files mention a copyright from 2014...
Yes, this has been a long ongoing project that I am glad I am finally able to publish. I started this before turning the
wacom.ko driver into a HID one. This was my initial idea, and it fell short. I never published it for IP reasons.
I just had the green light from Wacom to release this work, so here it is.
