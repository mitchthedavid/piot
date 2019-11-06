

#install dependencies
import os
""" os.('sudo apt-get install -y git python3-pip python3-gpiozero adafruit-io')
os.('pip3 install python3-gpiozero adafruit-io') """

validType=False
validNumber=False

maxSensors=25




import json

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


adafruitUser=input("Please enter your Adafruit username: ")
adafruitKey=input("Please enter your Adafruit IO key: ")

sensorConfigData={}
sensorConfigData['sensors']=[]
sensorConfigData['sensors'].append({'type': 'boolean','number': numSensors})

adafruitConfigData={}
adafruitConfigData['adafruitInfo']=[]
adafruitConfigData['adafruitInfo'].append({'user': adafruitUser, 'key': adafruitKey})
try:
    os.remove('./data/configData.json')
    os.remove('./data/adafruitCredentials.json')
    print ("old config file found....")
    print ("overwriting...")
except:
    print ("no config file found....")
    print ("creating new config file...")

with open('./data/configData.json','w') as outfile:
    json.dump(sensorConfigData, outfile)

with open('./data/adafruitCredentials.json','w') as outfile:
    json.dump(adafruitConfigData, outfile)