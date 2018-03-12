#!/usr/bin/python3
import time # to include necessary time intervals between actions
import serial # to communicate to serial device 

# Using the serial package the connection to the device is configured:
# A default baudrate of 9600 is assumed
# if problems are found this might need to be configured with the panel in the device itself.

ser = serial.Serial(port='/dev/ttyUSB0',timeout=0.5)

# Next we define a function that sends a command to the device 

def sendtodev(command):
        ser.write((command+'\r\n').encode()) # To each string the right terminator is added, the string is encoded into bytes, and then written to the device.
        time.sleep(0.01)
        return ser.readline().decode()[:-2] # The serial port is read, and the bytes object is decoded into a string.

sendtodev('*RST\n') # this commands resets the device and puts it in a standard state

time.sleep(1)

print(sendtodev('*IDN?')) # Print IDN of device

queries=['*ESE?','*ESR?','*IDN?','*OPC?','*PSC?','*SRE?','*STB?','*TST?']; # List with queries
answers=[] # empty list for answers
errorCodes=[] # empty list for errors
csvText='' # string to save all results and errors
for query in queries: # iterate through the queries
        time.sleep(0.5)
        answer = sendtodev(query)
        answers.append(answer)
        errorCode = sendtodev('SYST:ERR?')
        errorCodes.append(errorCode)
        print("*"*10)
        print("query: %s\nanswer: %s\nerror: %s" % (query, answer, errorCode))
        print("*"*10)
        csvText+="%s,%s,%s\n"%(query,answer,errorCode)


with open('qna.csv','w') as f1: # save the results to disk
        f1.write(csvText)
