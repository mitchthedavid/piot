
#import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import json
inPins=[7,11,13,15,19,21,23]
outPins=[8,10,12,14,16,18,22]
try:
	with open('configData.txt') as json_file:
		sensorConfigData=json.load(json_file)
except:
		print("no config data found...\nexiting....")
		exit()


numSensors=sensorConfigData['sensors'][0]['number']
print(str(numSensors)+" sensors...") #'['number'])
for i in range(0, numSensors):
	print("initializing sensor " +str(i+1) + " to pin " +str(inPins[i]))
	print("initializing indicator " +str(i+1) + " to pin " +str(outPins[i])+"\n\n")


#GPIO.setwarnings(False) # Ignore warning for now
#GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
#GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
    
#while True: # Run forever
	# if GPIO.input(7) == GPIO.LOW:
	# 	GPIO.output(8, GPIO.LOW) # Turn on
	# 	#curs.execute("""INSERT INTO buttondata values(0,0,1)""")
	# if GPIO.input(7) == GPIO.HIGH:
	# 	GPIO.output(8, GPIO.HIGH)
	# 	#curs.execute("""INSERT INTO buttondata values(0,0,0)""")
		
	
