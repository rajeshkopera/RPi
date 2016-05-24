###########################################################
#
# Name		: stepper.py
# Author	: Rajesh Bhandari
# Date		: 20 March 2014
# Description	: test code for stepp motor demo
#
###########################################################

#!/usr/bin/env python
 
# Import GPIO library for Raspberry Pi
import RPi.GPIO as GPIO
import time
 
# Define GPIO signals to use
stepPins = []

# Define Full Step sequence
fullStepSeqLen = 4
fullStepSeq = []
fullStepSeq = range(0, fullStepSeqLen)
fullStepSeq[0] = [1,0,0,0]
fullStepSeq[1] = [0,1,0,0]
fullStepSeq[2] = [0,0,1,0]
fullStepSeq[3] = [0,0,0,1]
 
# Define Half Step sequence
halfStepSeqLen = 8
halfStepSeq = []
halfStepSeq = range(0, halfStepSeqLen)
halfStepSeq[0] = [1,0,0,0]
halfStepSeq[1] = [1,1,0,0]
halfStepSeq[2] = [0,1,0,0]
halfStepSeq[3] = [0,1,1,0]
halfStepSeq[4] = [0,0,1,0]
halfStepSeq[5] = [0,0,1,1]
halfStepSeq[6] = [0,0,0,1]
halfStepSeq[7] = [1,0,0,1]

 
class stepperMotor():
	def forward(self, delay=0.5, steps=None, Seq=halfStepSeq, SeqLen=halfStepSeqLen):
		# Start main loop
		StepCounter = 0
		while 1==1:
			# loop to set value of all 4 pins one by one
			for pin in range(0, 4):
				xpin = stepPins[pin]
				if Seq[StepCounter][pin]!=0:
					print " Step %i Enable %i" %(StepCounter,xpin)
					GPIO.output(xpin, True)
				else:
					GPIO.output(xpin, False)
		 
			StepCounter += 1
		 
			# If we reach the end of the sequence
			# start again
			if (StepCounter==SeqLen):
				StepCounter = 0
			if (StepCounter<0):
				StepCounter = SeqLen
		 
			# Wait before moving on
			time.sleep(delay)


	def reverse(self, delay=0.5, steps=None, Seq=halfStepSeq, SeqLen=halfStepSeqLen):
		# Start main loop
		StepCounter = 0
		while 1==1:
			# loop to set value of all 4 pins one by one
			for pin in range(0, 4):
				xpin = stepPins[pin]
				if Seq[SeqLen-StepCounter-1][pin]!=0:
					print " Step %i Enable %i" %(StepCounter,xpin)
					GPIO.output(xpin, True)
				else:
					GPIO.output(xpin, False)
		 
			StepCounter += 1
		 
			# If we reach the end of the sequence
			# start again
			if (StepCounter==SeqLen):
				StepCounter = 0
			if (StepCounter<0):
				StepCounter = SeqLen
		 
			# Wait before moving on
			time.sleep(delay)
		


def main():
	
	global stepPins

	# Use BCM GPIO references
	# instead of physical pin numbers
	GPIO.setmode(GPIO.BCM)

	# decide which GPIO pins to use
	stepPins = [14,15,17,18]

	# Set all pins as output
	for pin in stepPins:
		print "Setup pins"
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin, False)

	motor = stepperMotor()

	motor.forward()
#	motor.reverse()	


if __name__ == "__main__":
    main()


