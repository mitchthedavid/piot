validType=False
validNumber=False

maxSensors=25

import json
import os
import getpass
username = getpass.getuser()


while validType == False or validNumber == False:
    try:
        numSensors=int(input("Please enter the number of boolean sensors: "))
        if numSensors<28 and numSensors>0:
            validType=True
            validNumber=True
    except:
        print ("not valid, please try again") 

adafruitKey=input("Please enter your Adafruit IO key: ")

sensorConfigData={}
sensorConfigData['sensors']=[]
sensorConfigData['sensors'].append({'type': 'boolean','number': numSensors})

adafruitConfigData={}
adafruitConfigData['adafruitInfo']=[]
adafruitConfigData['adafruitInfo'].append({'user': username, 'key': adafruitKey})
try:
    os.remove('configData.txt')
    os.remove('adafruitData.txt')
    print ("old config file found....")
    print ("overwriting...")
except:
    print ("no config file found....")
    print ("creating new config file...")

with open('configData.txt','w') as outfile:
    json.dump(sensorConfigData, outfile)

with open('adafruitData.txt','w') as outfile:
    json.dump(adafruitConfigData, outfile)