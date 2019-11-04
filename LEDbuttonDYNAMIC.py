
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import json
import time
from datetime import datetime

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

print("connecting to adafruit")
# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError

# Create an instance of the REST client.
aio = Client(username,key)
print("connected to adafruit...")


#get number of sensors from config file
numSensors=sensorConfigData['sensors'][0]['number']
print(str(numSensors)+" sensors...") #'['number'])

#start configuring gpio pins
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
for i in range(0, numSensors):
	print("initializing sensor " +str(i+1) + " to pin " +str(inPins[i]))
	
	print("initializing indicator " +str(i+1) + " to pin " +str(outPins[i])+"\n\n")
	
GPIO.setup(inPins[0:numSensors], GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #initialize sensor pin
GPIO.setup(outPins[0:numSensors], GPIO.OUT, initial=GPIO.HIGH) #initalize output pin

#start listening for input
os.system('pinout')
print("starting listening for sensor input")
while True: # Run forever
	try:
		for i in range (0, numSensors):
			digital = aio.feeds('piot.sensor'+str(i+1))
			if GPIO.input(inPins[i]) == GPIO.LOW:
				GPIO.output(outPins[i], GPIO.LOW) # Turn on
				aio.send(digital.key, 1)
			else:
				aio.send(digital.key, 0)
				GPIO.output(outPins[i], GPIO.HIGH) # Turn off
	except Exception as e:
		file = open("errors.txt", 'w')
		file.write(e+''+str(datetime.now()))
		file.close()

time.sleep(5)
