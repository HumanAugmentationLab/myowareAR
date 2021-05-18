# myowareAR

This repository contains the code to connect a Myoware sensor to an Augmented Reality (AR) experience.

## Setting up Lab Streaming Layer

We use the [Lab Streaming Layer (LSL)](https://labstreaminglayer.readthedocs.io/) as a way to stream data from devices to our analysis and visualization pipeline.

### Setup

This guide assumes you are attempting to get this setup on a Raspberry Pi.  If you are working with X86 machine, then you probably don't need to bother with the ``liblsl`` step below.

Given a standard install of Raspbian, we found the following additional dependencies were necessary.

Additional Dependencies:
- cmake

#### liblsl

To build ``liblsl`` from source, run the following commands.

```
$ git clone --recurse-submodules https://github.com/sccn/labstreaminglayer
$ mkdir build
$ cd build
$ cmake ..
$ make
$ sudo make install
```

Once you've installed the library, make sure that ``/usr/local/lib`` is in your dynamic library loading path.

```
$ echo "export LD_LIBRARY_PATH=/usr/local/lib:\$LD_LIBRARY_PATH" >> ~/.bashrc
$ source ~/.bashrc
```

Due to a bug in ``pylsl``, which we'll setup next, you'll need to create a sym link from ``liblsl.so`` to ``liblsl32.so`` so that ``pylsl`` can find the ``liblsl`` library.

```
$ sudo ln -s /usr/local/lib/liblsl.so /usr/local/lib/liblsl32.so
```

#### pylsl

You can install Python bindings for ``liblsl`` using pip.

```
$ pip3 install pylsl
```

### Running

Make sure that the Arduino Nano is plugged into the USB port of the Raspberry Pi.  You may need to reboot the Pi if the device does not show up.  You can tell if the device is visible by checking the ``/dev`` folder.  You should see a device in there that looks something like ``/dev/ttyUSB0``.

To stream the data to the lab streaming layer, run the SendData.py script (if the Nano is connected to another USB serial device, you'll need to substitute it for ``/dev/ttyUSB0`` in the example below).

```
$ ./SendData.py --device=/dev/ttyUSB0
```
