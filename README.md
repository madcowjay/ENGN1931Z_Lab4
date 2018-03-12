# lab4
Instrument control with Serial communication and SCPI commands.

Our goal for Lab 4 is to apply our knowledge of SCPI commands to first get up to speed on a new instrument given its manual, and second to take over the display of one of them to make a little clock.

Specifically, we will be working with one of the following instruments:

1. Agilent/HP/Keysight 33120A Function Generator [PDF manual](http://www.keysight.com/upload/cmc_upload/All/6C0633120A_USERSGUIDE_ENGLISH.pdf?&cc=US&lc=eng)
2. Agilent/HP/Keysight A34401 Digital Multimeter [PDF manual](http://galaxy.agh.edu.pl/~jena/INTEGRACJA/GPIB/34401-90004.pdf)

## Part 1: the parsing

Building off of your recent hwParsing assignment and your knowledge of RS-232, you will need to setup serial communication with one of the devices listed above and query its full state.

To help in this effort, we have included two starter codes:

`lab4_testIDN.py` is a script that allows you to quickly test a serial connection and send commands.

`lab4_qna.py` is a starter code that can help automate the question/answer process and produce a convenient CSV output.

Be sure to read the comments included in these Python scripts, for next you'll have to code something along the same lines.

After having parsed the manual and acquired a list of query commands, write a Python script that will query them all. Don't send a single command string (as in the HW) to the instrument, but rather one by one. Take inspiration from `lab4_qna.py`.

If your instrument beeps an error, remember that there is also a query command to find out the code for the produced errors. Use this to debug your interaction with the instrument.

## Part 2: the clock

Now you must consult the manual of the device you received, learn how to send text to be shown in the display, and write a program that turns it into a clock much like the one shown below. In the manual search for *DISPLAY*. Be mindful that the instrument must be set in *remote* mode to allow use of the display. 

In doing this you might find useful the Python packages: `time`, `datetime`, and `serial`.
To format the message to be sent, and adequately pad it with zeros, [this](https://stackoverflow.com/questions/339007/nicest-way-to-pad-zeroes-to-string) **stackoverflow** question might come in handy. 

Structure your code by: setting up the serial connection to the device, writing a function that returns a parsed string for the current time, writing a function that receives a string and sends it to the display, and running an infinite loop that regularly sends the current time to the display. Commands must not be sent too often to the instrument, add some latency in your loop.

[![Serial clock](https://img.youtube.com/vi/MsdK30OPvr8/0.jpg)](https://www.youtube.com/watch?v=MsdK30OPvr8)
