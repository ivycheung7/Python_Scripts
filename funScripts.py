#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

from PIL import Image, ImageDraw, ImageFont
import random, string

from time import strftime, gmtime
import datetime, time, sys

"Script returns and displays the links to each top trending projects from GitHub."
def displayGithubTrendingProjects():

    print(strftime("%A, %b %d, %Y %I:%M%p", gmtime()))
    html = requests.get("https://github.com/trending")
    soup = BeautifulSoup(html.text, "html.parser")
    urlList = []

    for header in soup.find_all('h3'):
        for url in header.find_all('a'):
            print(str('https://github.com' + url.get('href')))
            urlList.append(str('https://github.com' + url.get('href')))

    return urlList

"Creates a rip-off of Gmail icons. Alignments need work"
def createLetterIcon():

    isColorBright = False

    name = input("Enter your name\n")
    firstCharInName = name[0].upper()

    r = random.randrange(0,255,1)
    g = random.randrange(0,255,1)
    a = random.randrange(0,255,1)

    if (r&g&a > 160):
        isColorBright = True

    font = ImageFont.truetype( "TitilliumWeb-Regular.ttf", 140)
    icon = Image.new('RGBA', (256,256), (r,g,a,0))
    canvas = ImageDraw.Draw(icon)

    if isColorBright == False:
        canvas.text((85,20), firstCharInName,(255,255,255,0), font)
    else:
        canvas.text((85,20), firstCharInName,(0,0,0,0), font)

    canvas = ImageDraw.Draw(icon)    
    icon.show()

"Creates/Overwrite today's file to write attendance information in."
def checkIn():

    print("Type in 0 to stop taking attendance.")

    totalCount = 0;
    
    with open("attendance-" + str(datetime.date.today()) + ".csv", 'w') as attendance:
        attendance.write("Day, Date,Time,Full Name\n")
        while(True):
            name = input("Enter your full name.(" + str(totalCount) + ") currently in attendance.\n");
            if (name == "0"):
                break;
            totalCount += 1
            attendance.write(str(strftime("%A, %Y-%m-%d,%I:%M%p", gmtime()) + "," + name + '\n'));
        attendance.close();

    readFile()

'Reads and prints the data collected line-by-line'
def readFile():

    print('Opening file: "attendance-' + str(datetime.date.today()) + '.csv"\n')

    with open("attendance-" + str(datetime.date.today()) + ".csv", 'r+') as attendance:
        for line in attendance:
            print(line)

    attendance.close()

'Welcome to my one stop shop! For... currently three Python scripts'
def menu():    

    print("Hi there!")
    
    while(True):
        selection = input("What script would you like to run?\n1. Attendance CSV \n2. Create Gmail Icon \n3. Display Github Trending Projects \n0. I want to leave\n")
        if(selection == "0"):
            print("You disappoint me")
            break;
        elif(selection == "1"):
            checkIn()
        elif(selection == "2"):
            createLetterIcon()
        elif(selection == "3"):
            displayGithubTrendingProjects()
        else:
            print("Why are you so difficult?")

menu()
