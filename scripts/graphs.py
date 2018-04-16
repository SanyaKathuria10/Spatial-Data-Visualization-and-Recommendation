import pandas as pd

df = pd.read_csv("../data/data-ny.csv", sep = ',', header=None, names =  ['userid', 'venueid', 'venuecatid', 'venuecatname','latitute','longitude','timezone','utctime'])

time = df['utctime']

time = pd.to_datetime(time)

month = []

day = []

hour =[]

for i in time:

    month.append(i.month)

    hour.append(i.hour)

    day.append(i.weekday())


df['day'] = day

df['month'] = month

df['hour'] = hour

pd.DataFrame({'count' : df.groupby(['day', 'month', 'hour']).size()}).reset_index()