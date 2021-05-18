# myowareAR

This repository contains the code to connect a Myoware sensor to an Augmented Reality (AR) experience.

## Setting up Lab Streaming Layer

### Setup

Dependencies:
- cmake

#### liblsl

```
$ git clone --recurse-submodules https://github.com/sccn/labstreaminglayer
$ mkdir build
$ cd build
$ cmake ..
$ make
$ make install
```

Make sure ``/usr/local/lib`` is in your dynamic library loading path.

```
$ echo "export LD_LIBRARY_PATH=/usr/local/lib:\$LD_LIBRARY_PATH" >> ~/.bashrc
```

Due to a bug in ``pylsl``, which we'll setup next, you'll need to create a sym link so it can find the liblsl library.

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
``
