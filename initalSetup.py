validType=False
validNumber=False

maxSensors=25

import json
import os

while validType == False or validNumber == False:
    try:
        numSensors=int(input("Please enter the number of boolean sensors: "))
        if numSensors<28 and numSensors>0:
            validType=True
            validNumber=True
    except:
        print ("not valid, please try again") 

sensorConfigData={}
sensorConfigData['sensors']=[]
sensorConfigData['sensors'].append({'type': 'boolean','number': numSensors})

try:
    os.remove('configData.txt')
    print ("old config file found....")
    print ("overwriting...")
except:
    print ("no config file found....")
    print ("creating new config file...")

with open('configData.txt','w') as outfile:
    json.dump(sensorConfigData, outfile)