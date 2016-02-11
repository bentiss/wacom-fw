# TODO list

## Documentation
- Actually document the firmware format (both in this project and in the kernel commit description and code)

## Missing features
- support of the PADs buttons for bamboos tablets (see Bamboo later)
- ~~support for LEDs (in the descriptors and matching support in the kernel)~~
- ~~support for versioning embedded in the firmware directly (see versioning, later)~~
- ~~overwrite the name of the devices through the firmware~~
- tag which report descriptor is for which interface (touch, pad, pen) (see tagging report descriptors later)
- eventually add other interesting elements not easily described through the report descriptors (like .ovid in wacom_features)
- ~~add a checksum mechanism to prevent alteration/misreading of firmwares (see checksums)~~
- make sure we are forward compatible (see forward compatibility)
- make sure there are no attacks possible

### Bamboo
Bamboo devices have touch support through the Wacom internal touch protocol.
I was able to map the touch protocol to the current touch kernel recognition engine, but the pads events are interleaved
whithin the touch events. This doesn't work which means I can not support Bamboos for now.

### Versioning (done)
I'd like to provide a versioning mechanism based on git:
- if there is a tag attached to the current HEAD, I want the firmware to grab this tag athe version
- if not, I want the firmware to grab the last tag and append the short commit sha.
- when the tree is not clean, mark as such

The idea is that if the kernel outputs this information, we know exactly which commit produced the firmware.
We will be able to spot whether or not a user needs updating or not. Also, the good point is that the laziest me will
not have to keep incrementing versions for each devices at each modification :)

##### Update:
`git describe --tags --dirty=+` does exactly that :)

### Tagging report descriptors
I want to be able to tag which report descriptor is for which interface.
The current state is that we match the current report descriptor provided by the hardware to check whether or not the current
one we are processing is a match. 

This work fine for actual USB devices. However, for devices connected through the Wacom Wireless Receiver, the only
information we have is the PID of the connected device. It would be good to be able to fetch from the firmware the "touch"
report descriptor, or the "pad" one, or the "pen" one.

### Checksums (done)
The idea of having a checksum should prevent a corrupted firmware to be loaded and used by the kernel.
People should be able to alter the firmware, but this should result in the version not being similar to a released one.
So I think we should force people to use this project to make any modifications in the firmwares so we can track which
firmware comes from.

### Forward compatibility
I want to be sure that we do not have to do some weird dance in the kernel to support future firmware file format versions.
It means that any code put in the kernel should be able to read any firmware, written in the past and in the future.

A solution could be to explicitely request a firmware file format from the kernel, but I do not think it is good (especially
with distributions which cost is great when we want to update the kernel).

So I am thinking that we need a file format which is auto-descriptive.
The current implementation consists in having a tag (one char), then a 32 bits integer which tells the length of the field.
It is fine I think regarding forward compatibility, as long as we can ignore new tags, or not making them mandatory.

We should also be able to pack structs in the firmwares, but they should be versioned and extending them should not break
the ABI for older kernels.
