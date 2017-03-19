#!/usr/bin/env python

import datetime, time, sys;

def checkIn():
    "Creates/Overwrite file to write attendance information in. Format = 'Date, Name'"
    flag = False;
    print "This is an attendance script which creates a .csv once you exit the script.\n"
    with open("attendance-" + str(datetime.date.today()) + ".csv", 'wb') as attendance:
        attendance.write("Date,Full Name\n")
        while(flag == False):
            name = raw_input("Input your full name. Type in '0' to end.\n");
            if (name == "0"):
                flag = True;
                break;
            attendance.write(str(datetime.datetime.now()) + "," + name + '\n');
        attendance.close();

def readFile():
    'Reads and prints the data collected line-by-line'
    with open("attendance-" + str(datetime.date.today()) + ".csv", 'r+') as attendance:
        for line in attendance:
            print line;
    attendance.close();

checkIn()
readFile()

