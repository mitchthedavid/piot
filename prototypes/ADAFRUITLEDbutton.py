print("connecting to adafruit io...")
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time


# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError
ADAFRUIT_IO_USERNAME = "mitchdavid"
ADAFRUIT_IO_KEY = "0130d211fc4d4fe9a1f6caa69b350f7d"

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
digital = aio.feeds('piot.sensor1')

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(8, GPIO.OUT, initial=GPIO.HIGH) # Set pin 8 to be an output pin and set initial value to low (off)

print("connected.")

while True: # Run forever
    if GPIO.input(7) == GPIO.LOW:
        GPIO.output(8, GPIO.HIGH) # Turn on
        #aio.send(digital.key, 0)

    if GPIO.input(7) == GPIO.HIGH:
        GPIO.output(8, GPIO.LOW)
        aio.send(digital.key, 1)

    time.sleep(10)
		
		
	
