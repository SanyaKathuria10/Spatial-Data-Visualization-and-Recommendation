import pandas as pd

data = pd.read_csv("../data/data-ny.csv", sep = ',', header=None, names =  ['userid', 'venueid', 'venuecatid', 'venuecatname','latitude','longitude','timezone','utctime'])

checkin = pd.read_csv("../data/ny-checking-count.csv", sep = ",", header=True)

