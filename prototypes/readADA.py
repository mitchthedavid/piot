import json
import requests


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

from Adafruit_IO import Client, Feed, RequestError
aio = Client(username,key)
feeds=aio.feeds()
print("connected to adafruit...")



myData=[]
for feed in feeds:
	print(feed.key)
	
""" url = 'https://jsonplaceholder.typicode.com/todos/1' 
response = requests.get(url)        # To execute get request 
print(response.status_code)     # To print http response code  
print(response.text)            # To print formatted JSON response 

file = open("adaresults.txt", 'w')
file.write(response.text)
file.close() """

url = "https://io.adafruit.com//api/v2/mitchdavid/feeds/piot.sensor1/data"
response = requests.get(url)        # To execute get request 
print(response.status_code)     # To print http response code  
#print(response.text)            # To print formatted JSON response 

sensor1data=json.loads(response.text)
#print (sensor1data[0])
keysList=[]
downloadedData=keysList
for i in sensor1data[0]:
	keysList.append(i)

values=[]
timestamps=[]
for point in sensor1data:
	values.append(point['value'])
	timestamps.append(point['created_at'])
	

print (values,timestamps)








#https to file
""" outfile="sensor1data.json"
with open('sensor1data.json','w') as outfile:
    json.dump(response.text, outfile)

with open('sensor1data.json') as json_file:
		sensor1Data=json.load(json_file) """

