import json
import requests


try:
	with open('configData.txt') as json_file:
		sensorConfigData=json.load(json_file)
	with open('adafruitData.txt') as json_file:
		adafruitConfigData=json.load(json_file)
except:
		print("no config data found...\nexiting....")
		exit()

#get the adafruit info
username=adafruitConfigData['adafruitInfo'][0]['user']
key=adafruitConfigData['adafruitInfo'][0]['key']

print("connecting to adafruit")

from Adafruit_IO import Client, Feed, RequestError
aio = Client(username,key)
feeds=aio.feeds()
print("connected to adafruit...")
from pprint import pprint

myData=[]
for feed in feeds:
	print(feed.key)
	#print(aio.feeds(feed[1]))
	#myData.append(aio.feeds(feed.key))
	url="http://api/v2/"+username+"/feeds/"+feed.key+"/data"
	print(url)
	response = requests.get(url,params={'include':'value'})
	myData.append(response)
url1= 'https://jsonplaceholder.typicode.com/todos/1'
url="https://io.adafruit.com//api/v2/mitchdavid/feeds/piot.sensor1/data"
response = requests.get(url,params={'include':'value'})        # To execute get request 
#print(response.status_code)     # To print http response code  
#print(response.text)   
print (myData)
#print("connecting to GitHub API....")
#requests.get('https://api.github.com')
#print("connected to GitHub API....")


