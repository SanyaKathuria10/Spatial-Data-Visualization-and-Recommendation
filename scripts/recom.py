import pandas as pd
import math
from scipy.spatial import ConvexHull
import numpy as np
from sklearn.cluster import DBSCAN
import sys

def get_rows_by_category(df, category):
	#select all rows with category coffee shop
	category_rows = df.loc[df['venuecatname'] == category]
	return category_rows

def get_checkin_count_per_venue_in_category(category_rows):
	#get check incount of each venue with category coffee shop
	temp = category_rows
	time = pd.to_datetime(temp['utctime'])
	hour = []
	for i in time:
		hour.append(i.hour)
	temp.is_copy = False
	temp['hour'] = hour
	category_rows.is_copy = False
	category_rows["count"] =""
	category_rows["avg_time"] =""
	venue_group = temp.groupby(['venueid','longitude', 'latitude'])['hour'].agg({'count':'count', 'avg_time': 'mean'}).reset_index()
	#venue_group = pd.DataFrame({'count' : temp.groupby(['venueid', 'latitude', 'longitude']).size()}).reset_index()
	venue_group = venue_group.sort_values(['count'], ascending=False)
	return venue_group

def get_number_of_venues_per_category(venue_group):
	#count number of venues per category
	count_venue = len(venue_group['venueid'])
	return count_venue

def get_sorted_user_checkin_count_at_venues(category_rows):
	#count of how many times a user has gone to a particular venue
	user_venue_group = pd.DataFrame({'count' : category_rows.groupby(['userid','venueid']).size()}).reset_index()
	user_venue_group = user_venue_group.sort_values(['count'], ascending=False)
	return user_venue_group

def get_number_venues_visited_by_user(user_venue_group, user):
	print("in 5")
	user_rows = user_venue_group.loc[df['userid'] == user]
	count_user_venue = len(set(user_rows['venueid']))
	return count_user_venue

def get_all_user_checkins(df, user):
	#list of all checkins made by a user
	user_rows = df.loc[df['userid'] == user]
	user_rows = pd.DataFrame({'count' : category_rows.groupby(['userid','venueid','latitude','longitude']).size()}).reset_index()
	return user_rows

def calculate_p_close(venue_group, user_rows):
	#number of checkins in venue radius / total number of checkins of each user
	x = 0
	d = []
	x = user_rows
	denom = sum(user_rows['count'])
	p_close = []
	for index, venue in venue_group.iterrows():
		user_rows = x
		for index, user in user_rows.iterrows():
			d.append(haversine_dist(venue['latitude'], venue['longitude'], user['latitude'], user['longitude']))
		user_rows['distance'] = d
		maxi = max(d)
		mini = min(d)
		d = []
		user_rows = user_rows.loc[user_rows['distance'] < (maxi - mini)/3]
		p_close.append(sum(user_rows['count'])/denom)
	return p_close
	
def haversine_dist(lat1, lon1, lat2, lon2):
	"""Calculate the Haversine distance between two geo co-ordiantes."""
	radius = 3959  # miles
	dlat = math.radians(lat2 - lat1)
	dlon = math.radians(lon2 - lon1)
	
	a = math.sin(dlat / 2) * math.sin(dlat / 2) + \
	math.cos(math.radians(lat1)) \
	* math.cos(math.radians(lat2)) * \
	math.sin(dlon / 2) * math.sin(dlon / 2)
	
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
	d = radius * c
	return d

def calculate_p_like(category_rows, venue_group, time):
	#number of checkins at a venue / number of checkins at all venues belonging to the same category
	denom = sum(venue_group['count'])
	avg_time = pd.DataFrame({'average' : category_rows.groupby(['venueid'])['hour'].mean()}).reset_index()
	p_like = []
	#time penalty to make sure a place popular at nights is not suggested in the morning
	for index, venue in venue_group.iterrows():
		num = venue['count']
		initial_p_like = (num / denom)
		time_diff = abs(time - venue['avg_time'])
		if time_diff <= 3:
			penalized_p_like = initial_p_like
		elif time_diff <= 6:
			penalized_p_like = initial_p_like * 0.8
		elif time_diff <= 9:
			penalized_p_like = initial_p_like * 0.6
		elif time_diff <= 12:
			penalized_p_like = initial_p_like * 0.4
		else:
			penalized_p_like = initial_p_like * 0.2
		
		p_like.append(penalized_p_like)
	return p_like
	#distance between venue coordinates and each of user checkin, filter checkins using distance threshold and count #

def find_weights(user_rows):
	location = np.array(user_rows[['latitude', 'longitude']])
	hull = ConvexHull(location)
	return hull.volume

def suggestions(p_like, p_close, venue_group):
	w1 = 0.6
	x = np.array(p_like)
	y = np.array(p_close)
	p = w1 * x * y
	q = np.argsort(p)
	venueid = []
	end = 21 if len(q)>=21 else len(q)
	for i in range(1,end):
		index = q[i]
		venueid.append(venue_group.loc[index])
	print('\n')
	print("The suggested venueids for you are:")
	for venue in venueid:
		print(venue.venueid)


if __name__ == '__main__':
	df = pd.read_csv("../data/data-ny.csv", sep = ',', header=None, names =  ['userid', 'venueid', 'venuecatid', 'venuecatname','latitude','longitude','timezone','utctime'])
	category = sys.argv[1]
	user = int(sys.argv[2])
	time = int(sys.argv[3])
	category_rows = get_rows_by_category(df, category)
	venue_group = get_checkin_count_per_venue_in_category(category_rows)
	count_venue = get_number_of_venues_per_category(venue_group)
	user_venue_group = get_sorted_user_checkin_count_at_venues(category_rows)
	count_user_venue = get_number_venues_visited_by_user(user_venue_group, user)
	user_rows = get_all_user_checkins(df, user)
	p_close = calculate_p_close(venue_group, user_rows)
	p_like = calculate_p_like(category_rows, venue_group, time)
	suggestions(p_like, p_close, venue_group)
