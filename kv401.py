#!/usr/bin/python

import serial
import argparse


parser = argparse.ArgumentParser(description="Control KCEVE KVM401 switch over RS232")

parser.add_argument('kvmport', type=int, choices=range(1,5), help='KVM Port to select [1-4]')
parser.add_argument('-p', '--port', type=str, default='/dev/ttyUSB0', help="Serial port (default=/dev/ttyUSB0")
parser.add_argument('-b', '--baud', type=int, default=9600, help='Baudrate (default=9600)')

args = parser.parse_args()

ser = serial.Serial(args.port, args.baud, timeout=1)

msg = 'G0{}gA'.format(args.kvmport)
ser.write(msg.encode())

ser.flush()

ser.close()
