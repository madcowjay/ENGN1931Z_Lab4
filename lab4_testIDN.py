#!/usr/bin/python3
import time # to include necessary time intervals between actions
import serial # to communicate to serial device 

# Using the serial package the connection to the device is configured:
# A default baudrate of 9600 is assumed
# if problems are found this might need to be configured with the panel in the device itself.

deviceName=input('Please enter device path (e.g., /dev/ttyUSB0)\n')

if deviceName=='':
        deviceName='/dev/ttyUSB0'

ser = serial.Serial(port=deviceName,timeout=0.5)

# Next we define a function that sends a command to the device 

def sendtodev(command):
        ser.write((command+'\r\n').encode()) # To each string the right terminator is added and the string is encoded into bytes.
        time.sleep(0.01)
        return ser.readline().decode()[:-2] # The serial port is read, and the bytes object is decoded into a string.

print(sendtodev('*IDN?')) # Print IDN of device

# Do an infinite loop that allows for additional commands to be send to the device
while True:
        com=input('Enter Command:')
        if com=='': break
        print(sendtodev(com))
