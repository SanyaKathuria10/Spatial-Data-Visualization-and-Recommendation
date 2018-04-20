import pandas as pd
import math
from scipy.spatial import ConvexHull
import numpy as np


def get_list_of_users(df):
	users = pd.DataFrame({'count' : df.groupby(['userid']).size()}).reset_index()
	# users = df['userid'].unique()
	# print(users[0])
	#user_rows = df.loc[df['userid'] == users['userid'][0]]
	#print(users[1:2].userid)
	return users

def get_category_rows(df):
	category_rows = df.loc[df['venuecatname'] == category]
	return category_rows

def get_user_rows(df, user):
	user_rows = df.loc[df['userid'] == user]
	#print(user_rows.head())
	return user_rows

def get_average_users_per_venue():
	user = pd.DataFrame({'count' : df.groupby(['userid']).size()}).reset_index()
	#print(len(user))

	venue = pd.DataFrame({'count' : df.groupby(['venueid']).size()}).reset_index()
	#print(len(venue))

	avg = len(venue) / len(user)
	#print(avg)
	return avg

def get_sorted_user_checkin_count_at_venues(category_rows):
	#count of how many times a user has gone to a particular venue
	user_venue_group = pd.DataFrame({'count' : category_rows.groupby(['userid','venueid']).size()}).reset_index()
	user_venue_group = user_venue_group.sort_values(['count'], ascending=False)
	return user_venue_group

def get_checkins_per_venue(category):
	venue_checkins = pd.DataFrame({'count' : category_rows.groupby(['venueid', 'latitude', 'longitude']).size()}).reset_index()	
	return venue_checkins

def get_users_visited_venue(user_venue_group):
	venue_user = dict()
	for row in user_venue_group.iterrows():
	    if row[1].venueid in venue_user:
	        s = set()
	        s = venue_user[row[1].venueid]
	        s.add(row[1].userid)
	        venue_user[row[1].venueid] = s
	    else:
	        s = set()
	        s.add(row[1].userid)
	        venue_user[row[1].venueid] = s

def define_alpha():
	alpha = {
	    'food': 1.64,
	    'nightlife': 1.61,
	    'travel': 2.22,
	    'work': 1.62,
	    'home': 1.62,
	    'shops': 1.64,
	    'entertainment': 1.64,
	    'art': 1.64,
	    'parks': 1.68,
	    'education': 1.96
	}
	return alpha

def center_of_mass(users, df):
    avg_lat = []
    avg_long = []
    _users = users
    for index, row in _users.iterrows():
        user_rows = df.loc[df['userid'] == row['userid']]
        avg_lat.append(pd.DataFrame.mean(user_rows['latitude']))
        avg_long.append(pd.DataFrame.mean(user_rows['longitude']))
    print(avg_lat[:5])
    _users['latitude'] = avg_lat
    _users['longitude'] = avg_long
    return _users

def get_lat_long(venueid, venue_checkins):
    row = venue_checkins.loc[venue_checkins['venueid'] == venueid ]
    #print(row)
    return row['latitude'], row['longitude']

def haversine_dist(lat1, lon1, lat2, lon2):
    """Calculate the Haversine distance between two geo co-ordiantes."""
    radius = 3959  # miles
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c
    return d

def get_distance_from_center_of_mass():
	dist = []
	for row in range(0,len(x)):
    	dist.append(haversine_dist(com['latitude'][row], com['longitude'][row], venue_lat, venue_long))
    return dist

def calc_p_close(dist):
	p_close = [1 / x ** 1.64 for x in dist]
	return p_close

if __name__ == '__main__':
	df = pd.read_csv("../data/data-ny.csv", sep = ',', header=None, names =  ['userid', 'venueid', 'venuecatid', 'venuecatname','latitude','longitude','timezone','utctime'])
	category = "Coffee Shop"
	venueid = '4ab966c3f964a5203c7f20e3'
	user = 642
	time = 16