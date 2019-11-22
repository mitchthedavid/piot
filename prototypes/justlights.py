
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import json
import time
inPins=[7,11,13,15,19,21,23]
outPins=[8,10,12,14,16,18,22]

	print("initializing sensor " +str(i+1) + " to pin " +str(inPins[i]))
	

	
GPIO.setup(inPins[0:numSensors], GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #initialize sensor pin
GPIO.setup(outPins[0:numSensors], GPIO.OUT, initial=GPIO.HIGH) #initalize output pin

#start listening for input
print("starting listening for sensor input")
while True: # Run forever
    
	for i in range (0, numSensors):
		#digital = aio.feeds('piot.sensor'+str(i+1))
		#if GPIO.input(inPins[i]) == GPIO.LOW:
		GPIO.output(outPins[i], GPIO.HIGH) # Turn on
			#aio.send(digital.key, 0)
		#else:
		time.sleep(1)
			#aio.send(digital.key, 1)
		GPIO.output(outPins[i], GPIO.LOW) # Turn off

		
