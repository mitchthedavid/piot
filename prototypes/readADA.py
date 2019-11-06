import json
import requests
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

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


from Adafruit_IO import Client, Feed, RequestError
#log into adafruit
aio = Client(username,key)
feeds=aio.feeds() #grabs a list of feeds that you have
print("connected to adafruit...")
feedList=[]#holds the feeds
downloadedData=[] #hold the data
for feed in feeds:
	feedKey=feed.key
	feedList.append(feedKey)
	print(str(feedKey)+str(feed))
	#run a request to get the data for each feed
	url = "https://io.adafruit.com//api/v2/mitchdavid/feeds/"+str(feedKey)+"/data"
	response = requests.get(url)        # To execute get request 
	downloadedData.append(json.loads(response.text)) #load the data
for feed in downloadedData:
	print(feed)

print("exit")
""" values=[]
timestamps=[]
for point in sensor1data:
	values.append(point['value'])
	timestamps.append(point['created_at']) """
	

""" print (values,timestamps)
# Data for plotting
fig, ax = plt.subplots()
ax.plot(timestamps, values)

ax.set(xlabel='time (s)', ylabel='position',
       title='sensor1 data')
ax.grid()

fig.savefig("test.png")
#plt.show() """








#https to file
""" outfile="sensor1data.json"
with open('sensor1data.json','w') as outfile:
    json.dump(response.text, outfile)

with open('sensor1data.json') as json_file:
		sensor1Data=json.load(json_file) """

