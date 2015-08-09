#! /usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 19:51:53 2015

@author: omancarci
"""


import RPi.GPIO as GPIO
import configparser
import time
import smtplib

config = configparser.ConfigParser()
config.read('.config')
buttonIn = int(config['piConfig']['buttonIn'])
lightOut = config['piConfig']['lightOut']
if len(lightOut)>0:
    lightOut = int(lightOut)

sender = config['gmailInfo']['sendermail']
receiver = config['gmailInfo']['receivermail']
password = config['gmailInfo']['password']
message = config['gmailInfo']['message']



GPIO.setmode(GPIO.BCM)

GPIO.setup(buttonIn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(lightOut, GPIO.OUT)

while True:
    input_state = GPIO.input(buttonIn)
    if input_state == False:
        print('Button Pressed')
        GPIO.output(lightOut, GPIO.HIGH)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender,receiver,message)
        server.quit()
        time.sleep(0.5)
        GPIO.output(lightOut, GPIO.LOW)



