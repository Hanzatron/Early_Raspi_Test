#!/usr/bin/python

import RPi.GPIO as GPIO
import sleep

poort = 26


GPIO.setmode(GPIO.BCM) #Nummering van de poorten gebruiken zoals op printplaat
GPIO.setup(poort, GPIO.OUT)

GPIO.output(poort, True)
