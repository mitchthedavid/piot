import json

with open('configData.txt') as json_file:
    sensorConfigData=json.load(json_file)

print(sensorConfigData['sensors'][0]['number']) #'['number'])