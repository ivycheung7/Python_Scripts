#!/usr/bin/env python

from PIL import Image, ImageDraw, ImageFont
import random, string

def letterImage():
    "Creates a rip-off of Google email icons."
    letColor = False
    name = raw_input("What is your name? (SSN will be asked next. Then your bank account.)\n" )
    let = name[0].upper()
    r = random.randrange(0,255,1)
    g = random.randrange(0,255,1)
    a = random.randrange(0,255,1)
    if (r&g&a > 160):
        letColor = True #Light bg color & Light Letter color do not mix
    font = ImageFont.truetype( "georgiaz.ttf", 140)
    theImage = Image.new('RGBA', (256,256), (r,g,a,0))
    theLetter = ImageDraw.Draw(theImage)
    if letColor == False:
        theLetter.text((60,60), let,(255,255,255,0), font)
    else:
        theLetter.text((60,60), let,(0,0,0,0), font)
    theLetter = ImageDraw.Draw(theImage)    
    theImage.show()
    
letterImage()
