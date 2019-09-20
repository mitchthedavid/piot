print("hello button")
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
#import MySQLdb
#db = MySQLdb.connect("localhost", "pi", "raspberry", "button")
#curs=db.cursor()

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
    
while True: # Run forever
	if GPIO.input(7) == GPIO.LOW:
		GPIO.output(8, GPIO.LOW) # Turn on
		#curs.execute("""INSERT INTO buttondata values(0,0,1)""")
	if GPIO.input(7) == GPIO.HIGH:
		GPIO.output(8, GPIO.HIGH)
		#curs.execute("""INSERT INTO buttondata values(0,0,0)""")
		
	
