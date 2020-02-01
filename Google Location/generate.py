import json
import csv
import os
import datetime

# where is your locationhistory.json file located?
fname = "./src/test.json"

# open and read the file
print('Reading location history JSON file...')
file = open(fname, "r")
content = file.read()
file.close()

# load the json to program
print('Loading JSON internally...')
data = json.loads(content)

# create the CSV
print('Creating your CSV file...')
fieldnames = ['timestamp, longitudeE7, latitudeE7, accuracy, altitude, verticalAccuracy, velocity']
w = open('./src/test.csv', 'w')
wr = csv.writer(w, delimiter=',')
wr.writerow(fieldnames)

# iterate through JSON to find the data we need
output = ""
outputCount = 0
count = len(data['locations'])
for c in range(0,count):

	# safely grab the data available in each json location index
	json_line = data.get('locations', [])
	time = datetime.datetime.fromtimestamp(int(json_line[c].get('timestampMs', 1000)) / 1000.0)
	lon = json_line[c].get('longitudeE7', -1) / 10000000
	lat = json_line[c].get('latitudeE7', -1) / 10000000
	acc = json_line[c].get('accuracy', -1)
	alt = json_line[c].get('altitude', -1)
	vAcc = json_line[c].get('verticalAccuracy', -1)
	vel = json_line[c].get('velocity', -1)

	# create and write the string to a row
	output = str(time) + "," + str(lon) + "," + str(lat) + "," + str(acc) + "," + str(alt) + "," + str(vAcc) + "," + str(vel);
	wr.writerow([output])
	outputCount += 1

w.close()
print('Done!')
