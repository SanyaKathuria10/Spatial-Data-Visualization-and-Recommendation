import pandas as pd
import operator

df = pd.read_csv("../data/data-ny.csv", sep = ',', header=None, names =  ['userid', 'venueid', 'venuecatid', 'venuecatname','latitude','longitude','timezone','utctime'])

venuecount = {}

f = open("ny-checkin-count.csv", 'w')
f1 = open("ny-sorted-checkin-count.csv", 'w')

for index, row in df.iterrows():
	if row['venueid'] in venuecount.keys():
		venuecount[row['venueid']] = venuecount[row['venueid']] + 1
	else:
		venuecount[row['venueid']] = 1


for x in sortedvenues.keys():
	f.write(str(x) + ',' + str(sortedvenues[x]) + '\n')
f.close()

sortedvenues = sorted(venuecount.items(), key=operator.itemgetter(1), reverse=True)

i = 0
while sortedvenues[i][1] >= 100:
        f1.write(str(sortedvenues[i][0]) + ',' + str(sortedvenues[i][1]) + '\n')
        i = i + 1
f1.close()