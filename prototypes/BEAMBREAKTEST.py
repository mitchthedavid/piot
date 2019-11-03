
# import call method from subprocess module 
from subprocess import call 

# import sleep to show output for some time period 
import time
import os 

# define clear function 
def clear(): 
    # check and make call for specific operating system 
    os.system('cls' if os.name == 'nt' else 'clear')


import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
#import MySQLdb
#db = MySQLdb.connect("localhost", "pi", "raspberry", "button")
#curs=db.cursor()

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
print("PIN 7 IS INPUT")
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
print("PIN 8 IS OUTPUT")
os.system('pinout')
myVar=input("PRESS ENTER TO CONTINUE...\n\n\n")
print("listening")
counter=0
while True: # Run forever
    if GPIO.input(7) == GPIO.LOW:
        GPIO.output(8, GPIO.LOW) # Turn on
        print("pin 7 is low")

    if GPIO.input(7) == GPIO.HIGH:
        GPIO.output(8, GPIO.HIGH)
        print("pin 7 is high")

    #counter+=1
    #if counter%50 == 0:
        #clear()    
    #time.sleep(2)
    #clear()
