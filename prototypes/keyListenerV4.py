import json
import csv 
from pynput import keyboard
from datetime import datetime,date
import matplotlib.pyplot as plt

import sys


colors=['r','g','b','c','y','m','k'] #as list so that colors can be looped through
sensorPressed=0
keyPressed=0 #keyPressed changes on key change. If key is not in range of sensors, defaults to 0

#read json config file


numSensors=3
#fill the press data with a number of blank arrays equal to the number  of sensors
pressData = [[] for _ in range(numSensors+1)] 
#fill the time data with a number of blank arrays equal to the number  of sensors
timeData = [[] for _ in range(numSensors+1)]

def on_press(key):    
    try:
        print ("key pressed") #indicates when key is pressed, comment out for speed
        keyPressed=int('{0}'.format(key.char))

        if len(pressData[keyPressed])>=1: #there needs to be at least two data points to compare to the previous entry
            timeElapsed=(datetime.now()-timeData[keyPressed][len(timeData[keyPressed])-1]).total_seconds()
            
            #add a  0 for readability if there is a significant amount of time before the current entry
            if timeElapsed>0.04 and pressData[keyPressed][len(pressData[keyPressed])-1]!=1:
                pressData[keyPressed].append(0)
                timeData[keyPressed].append(datetime.now())
        
        else: #this will capture the first time data is logged,(if len>=1) add a 0 to improve readbility
            pressData[keyPressed].append(0)
            timeData[keyPressed].append(datetime.now())
        
        #whenever the key is pressed
        pressData[keyPressed].append(1)
        timeData[keyPressed].append(datetime.now())
        
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    try:
        keyPressed=int('{0}'.format(key.char))
    except:
        keyPressed=0 #the 0th element in the data arrays is all garbage data, send it there
      
    #add a 1 to the array to increase readability
    pressData[keyPressed].append(1)
    timeData[keyPressed].append(datetime.now())
    
    pressData[keyPressed].append(0)
    timeData[keyPressed].append(datetime.now())

    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
print("key tracking is now active.")
if numSensors>0:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

else: #numSensors>0, cant have 0 sensors
   print ("piot is not properly configured. Run 'piot setup' to configure your installation.")
   sys.exit()


for i in range(1,numSensors+1):
    #ensure all sensors end at 0 for readability
    pressData[i].append(0)
    timeData[i].append(datetime.now())


    #modulus(%) allows to loop through colors in case of more sensors than colors
    #doing the plot statement in the forloop allows multiple sensors to be logged
    plt.plot(timeData[i],pressData[i],c=colors[(i-1)%len(colors)],label="Sensor " + str(i))
    
    #add data label(s)
    pressData[i].insert(0,"Sensor "+ str(i))
    timeData[i].insert(0,"Time")
    
plt.legend(loc='lower left')
plt.show()
   
#remove 0th (garbage) data
del timeData[0]
del pressData[0]

#write data to file
""" with open("data.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    for i in range(0,numSensors):
        csvWriter.writerows([pressData[i],timeData[i]]) """