#######################################################################
#
# Author	:: Rajesh Bhandari
# Date		:: 19 MAr 2014
# Title		:: led.py
#
# Description	:: This code just blinks 4 LEDs one after other. 
# 		   The GPIOs used in this are 
#			- GPIO 14 :
#			- GPIO 15 :
#			- GPIO 17 :
#			- GPIO 18 :
#
#######################################################################

'''
	GPIO layout for Raspberry Pi

		3.3V	-------	X	O ------- 5V	
		GPIO 0	-------	O	O ------- 5V
		GPIO 1	-------	O	O ------- GND
		GPIO 4	-------	O	O ------- GPIO 14
		GND	-------	O	O ------- GPIO 15
		GPIO 17	-------	O	O ------- GPIO 18
		GPIO 21	-------	O	O ------- GND
		GPIO 22	------- O	O ------- GPIO 23
		3.3V	-------	O	O ------- GPIO 24
		GPIO 10	-------	O	O ------- GND
		GPIO 9	-------	O	O ------- GPIO 25
		GPIO 11	-------	O	O ------- GPIO 8
		GND	-------	O	O ------- GPIO 7
'''


# import the GPIO library for RPi
import RPi.GPIO as GPIO
import time

# Set the mode to Broadcom
GPIO.setmode(GPIO.BCM)

#set the direction of the GPIO pins
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

# Turn OFF all the pins
GPIO.output(14,False)
GPIO.output(15,False)
GPIO.output(17,False)
GPIO.output(18,False)

#
# infiniteloop
# toggle each pin serialy with 1 sec delay
#
var = 1
while var == 1 :
	GPIO.output(14,True)
	time.sleep(1)
	GPIO.output(14,False)
	time.sleep(1)
	GPIO.output(15,True)
	time.sleep(1)
	GPIO.output(15,False)
	time.sleep(1)
	GPIO.output(17,True)
	time.sleep(1)
	GPIO.output(17,False)
	time.sleep(1)
	GPIO.output(18,True)
	time.sleep(1)
	GPIO.output(18,False)
	time.sleep(1)
