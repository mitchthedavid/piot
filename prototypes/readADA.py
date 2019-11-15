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
feedList=[]#holds the feeds
downloadedData=[] #hold the data
#loop through each feed in the list of feeds
#grab the key for that feed
for feed in feeds:
	feedKey=feed.key
	feedList.append(feedKey)
	
	#run a request to get the data for each feed
	url = "https://io.adafruit.com//api/v2/mitchdavid/feeds/"+str(feedKey)+"/data"
	response = requests.get(url)        # To execute get request 
	downloadedData.append(response.content) #load the data
	numFeeds=len(downloadedData)

	
#convert each datapoint to a json object for pain free referencing
values=[]
for i in range(len(downloadedData)):
	downloadedData[i]=json.loads(downloadedData[i])#convert the data to a json object
	values.append([]) #add a sublist to values for each feed

#get the keys for each of the points (will need to update for boolean sensors)
#not important for mergring data into one list
keyList=[]
for key in downloadedData[0][0].keys():
	keyList.append(str(key))
#print ("each datapoint has the following attributes:")
#print(keyList)


#loop through the data and sort into ordered pairs
#sorted contains all the ordered pairs
allData=[]
d = defaultdict(int) #not sure what this does
for i in range(numFeeds-1): #each feed
	numPoints=len(downloadedData[i])
	for j in range(numPoints):#each point in that feed
		value=float(downloadedData[i][j]['value'])
		time=dateutil.parser.parse(downloadedData[i][j]['created_at'])
		values[i].append([time,value]) #each sublist in the values list consists of ordered pair from 1 feed
		allData.append([time,value]) #no need for sublisting in all data (list of all ordered pars)


#set up all the data into a timeseries
#############################
time = [*zip(*allData)][0]#series of time
value = [*zip(*allData)][1]#series of value
# Create an empty dataframe
df = pd.DataFrame()
# Create a column from the datetime variable
df['datetime'] = time
# Convert that column into a datetime datatype
df['datetime'] = pd.to_datetime(df['datetime'])
# Set the datetime column as the index
df.index = df['datetime'] 
# Create a column from the numeric value
df['value'] = value
df=df.resample('S').sum()
#print(df)
#df.plot(kind='bar',x='time',y='value')
##########################################	

		


fig, ax = plt.subplots()
#check them (or sort them maybe???idk) 
#convert to timeseries?????
#plot them??????????????????????
errors=[]
numPoints=[]
colors=["r","g","b"]

for i in range(numFeeds): #each feed
	numPoints.append(len(downloadedData[i]))
	ax.plot(*zip(*values[i]),colors[i%len(colors)])

#df.plot(ax=ax)#kind='line',x='time',y='value',)


ax.set(xlabel='time (s)', ylabel='position',title='Weight Rack Data')
ax.grid()


plt.show() 

print("exit")







#https to file
""" outfile="sensor1data.json"
with open('sensor1data.json','w') as outfile:
    json.dump(response.text, outfile)

with open('sensor1data.json') as json_file:
		sensor1Data=json.load(json_file) """

