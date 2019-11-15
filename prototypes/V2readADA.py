import json #to parse each data point
import requests #to pull data from the adafruit server
from datetime import datetime #to tell time and stuff
import dateutil.parser #to parse the weird date format ada uses
import matplotlib #plot
import matplotlib.pyplot as plt#plot
from collections import defaultdict#to merge the timeseries data for sensors
from Adafruit_IO import Client, Feed, RequestError #to access ada
import pandas as pd #timeseries analysis
from collections import OrderedDict #for pandas

#open the config files and get the username and key for ADA
try:
	with open('./data/configData.json') as json_file:
		sensorConfigData=json.load(json_file)
	with open('./data/adafruitCredentials.json') as json_file:
		adafruitConfigData=json.load(json_file)
except:
		print("no config data found...\nexiting....")
		exit()

#get the adafruit info
username=adafruitConfigData['adafruitInfo'][0]['user']
key=adafruitConfigData['adafruitInfo'][0]['key']

print("connecting to adafruit")


#log into adafruit
aio = Client(username,key)
feeds=aio.feeds() #grabs a list of feeds that you have (ada object)
print("connected to adafruit...")