import pandas as pd

#all of new york data
data = pd.read_csv("../data/data-ny.csv", sep = ',', header=None, names =  ['userid', 'venueid', 'venuecatid', 'venuecatname','latitude','longitude','timezone','utctime'])

#data containing each venue, venue information and number of checkins at that venue
checkin = pd.read_csv("../data/ny-checking-count.csv", sep = ",", header=True)

#user input of current location and time
latitude = 40.68
longitude = -73.98
time = 