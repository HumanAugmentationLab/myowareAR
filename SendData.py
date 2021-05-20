#!/usr/bin/env python3

"""Example program to demonstrate how to send a multi-channel time series to
LSL."""
import sys
import getopt
import serial
import time
from random import random as rand

from pylsl import StreamInfo, StreamOutlet, local_clock

def main(argv):
    name = 'Myoware'
    type = 'EEG'
    # clock, then 4 Analog values 
    n_channels = 4
    help_string = 'SendData.py -s <sampling_rate> -n <stream_name> -t <stream_type>'
    try:
        opts, args = getopt.getopt(argv, "hd:s:c:n:t:", longopts=["device=", "srate=", "channels=", "name=", "type"])
    except getopt.GetoptError:
        print(help_string)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(help_string)
            sys.exit()
        elif opt in ("-d", "--device"):
            device = arg
        elif opt in ("-s", "--srate"):
            srate = float(arg)
        elif opt in ("-c", "--channels"):
            n_channels = int(arg)
        elif opt in ("-n", "--name"):
            name = arg
        elif opt in ("-t", "--type"):
            type = arg
    srate = 500
    # first create a new stream info (here we set the name to BioSemi,
    # the content-type to EEG, 8 channels, 100 Hz, and float-valued data) The
    # last value would be the serial number of the device or some other more or
    # less locally unique identifier for the stream as far as available (you
    # could also omit it but interrupted connections wouldn't auto-recover)
    info = StreamInfo(name, type, n_channels, srate, 'float32', 'myuid34234')

    # next make an outlet
    outlet = StreamOutlet(info)

    print("now sending data...")
    start_time = local_clock()
    sent_samples = 0
    with serial.Serial(device, 500000) as ser:
        while True:
            elapsed_time = local_clock() - start_time
            vals = list(map(float, ser.readline().decode('utf8').split()))
            if len(vals[1:]) == n_channels:
                outlet.push_sample(vals[1:])
            else:
                print("malformatted line")
            print(vals)
            time.sleep(0.0001)

if __name__ == '__main__':
    main(sys.argv[1:])
