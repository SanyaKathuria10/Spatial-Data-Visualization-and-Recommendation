import pandas as pd
import operator

df = pd.read_csv("../data/data-ny.csv", sep = ',', header=None, names =  ['userid', 'venueid', 'venuecatid', 'venuecatname','latitude','longitude','timezone','utctime'])

venuecount = {}
venuedetails = {}

f = open("ny-checkin-count.csv", 'w')
f1 = open("ny-sorted-checkin-count.csv", 'w')

for index, row in df.iterrows():
	if row['venueid'] in venuecount.keys():
		venuecount[row['venueid']] = venuecount[row['venueid']] + 1
	else:
		venuecount[row['venueid']] = 1
		venuedetails[row['venueid']] = [row['latitude'], row['longitude']]
f.write('Venue ID, Latitude, Longitude, Checkin Count\n')
for x in venuecount.keys():
	f.write(str(x) + ',' + str(venuedetails[x][0]) + ',' +str(venuedetails[x][1]) + ',' +str(venuecount[x]) + '\n')
f.close()

sortedvenues = sorted(venuecount.items(), key=operator.itemgetter(1), reverse=True)

f1.write('Venue ID, Latitude, Longitude, Checkin Count\n')
i = 0
while i >= 100:
    f1.write(str(sortedvenues[i][0]) + ',' + str(venuedetails[sortedvenues[i][0]][0]) + ',' +str(venuedetails[sortedvenues[i][0]][1]) + ',' +str(sortedvenues[i][1]) + '\n')
    i = i + 1
f1.close()