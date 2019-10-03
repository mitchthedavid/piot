
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import json
import time
inPins=[7,11,13,15,19,21,23]
outPins=[8,10,12,14,16,18,22]
try:
	with open('configData.txt') as json_file:
		sensorConfigData=json.load(json_file)
	with open('adafruitData.txt') as json_file:
		adafruitConfigData=json.load(json_file)
except:
		print("no config data found...\nexiting....")
		exit()

#get the number of sensors
numSensors=sensorConfigData['sensors'][0]['number']

#get the adafruit info
username=adafruitConfigData['adafruitInfo'][0]['user']
key=adafruitConfigData['adafruitInfo'][0]['key']


# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError

# Create an instance of the REST client.
aio = Client(username,key)


#get number of sensors from config file
numSensors=sensorConfigData['sensors'][0]['number']
print(str(numSensors)+" sensors...") #'['number'])

#start configuring gpio pins
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
for i in range(0, numSensors):
	print("initializing sensor " +str(i+1) + " to pin " +str(inPins[i]))
	GPIO.setup(inPins[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #initialize sensor pin
	print("initializing indicator " +str(i+1) + " to pin " +str(outPins[i])+"\n\n")
	GPIO.setup(outPins[i], GPIO.OUT, initial=GPIO.HIGH) #initalize output pin

#start listening for input

while True: # Run forever
    
	for i in range (1, numSensors+1):
		digital = aio.feeds('sensor'+str(i))
	if GPIO.input(inPins[i]) == GPIO.LOW:
		GPIO.output(outPins[i], GPIO.HIGH) # Turn on
		aio.send(digital.key, 0)
	else:
		aio.send(digital.key, 1)

	time.sleep(1)
