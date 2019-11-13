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
jsonData=[] #downloadedData, but convereted to JSON (downloadedData[i][j]['created_at'])
values=[]
times=[]
#loop through each feed in the list of feeds
#grab the key for that feed
for feed in feeds:
    feedKey=feed.key
    feedList.append(feedKey)
    #run a request to get the data for each feed
    url = "https://io.adafruit.com//api/v2/mitchdavid/feeds/"+str(feedKey)+"/data"
    response = requests.get(url)        # To execute get request 
    downloadedData.append(response.content) #load the data
    values.append([])#create sublist
    times.append([])#create sublist

numFeeds=len(downloadedData)

#plot stuf####################################
fig, ax = plt.subplots()
colors=["r","g","b"]
################################


jsonData=downloadedData #convert to JSON in next loop
allPandaData=[]
data=[]

for i in range(numFeeds):
        jsonData[i]=json.loads(downloadedData[i])#convert each feed to a list of json object(s)
        numPoints=len( jsonData[i])
        data.append([])
        for j in range(numPoints): #loop through every point
                valueVal=jsonData[i][j]['value']
                values[i].append(valueVal)
                timeVal=dateutil.parser.parse(jsonData[i][j]['created_at'])
                #timeVal=jsonData[i][j]['created_at']
                times[i].append(timeVal)
                data[i].append([timeVal,valueVal])
        if len(times[i])>0:
                #set up all the data into a timeseries
                #############################
                time = times[i]#series of time
                value = values[i]#series of value
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
                #df=df.resample('S').sum()
                df.plot(ax=ax)
        ##########################################`	

#plot stuf####################################
ax.set(xlabel='time (s)', ylabel='position',title='Weight Rack Data')
ax.grid()
plt.show() 
################################       

print (feedList)