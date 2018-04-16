import pandas as pd
import math

def get_rows_by_category(df, category):
	#select all rows with category coffee shop
	category_rows = df.loc[df['venuecatname'] == category]
	return category_rows

def get_checkin_count_per_venue_in_category(category_rows):
	#get check incount of each venue with category coffee shop
	venue_group = pd.DataFrame({'count' : category_rows.groupby(['venueid', 'latitude', 'longitude']).size()}).reset_index()
	venue_group = venue_group.sort_values(['count'], ascending=False)
	return venue_group

#count number of venues
def get_number_of_venues_per_category(venue_group):
	count_venue = len(venue_group['venueid'])
	#print(count_venue)
	#38333
	return count_venue

def get_sorted_user_checkin_count_at_venues(category_rows):
	#count of how many times a user has gone to a particular venue
	user_venue_group = pd.DataFrame({'count' : category_rows.groupby(['userid','venueid']).size()}).reset_index()
	user_venue_group = user_venue_group.sort_values(['count'], ascending=False)
	return user_venue_group

def get_number_venues_visited_by_user(user_venue_group, user):
	#find all rows about that user
	user_rows = user_venue_group.loc[df['userid'] == user]
	count_user_venue = len(set(user_rows['venueid']))
	#print(count_user_venue)
	#105
	return count_user_venue

def get_all_user_checkins(df, user):
	user_rows = df.loc[df['userid'] == user]
	user_rows = pd.DataFrame({'count' : category_rows.groupby(['userid','venueid','latitude','longitude']).size()}).reset_index()
	return user_rows

def calculate_p_go(count_venue, count_user_venue):
	#calculalte the probability of the user going to the venue
	p_go = count_user_venue / count_venue
	return p_go
	#print(p_go)

def calculate_checkins_within_venue_radius(venue_group, user_rows):
	#total number of checkins of each user
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
	print(p_close[:10])
		#user_rows = user_rows['userid', 'venueid', 'latitude', 'longitude', 'count']
		# user_rows = user_rows.drop(labels = ['distance'], axis = 1)
		# print(user_rows.head())

		
	#distance between venue coordinates and each of user checkin, filter checkins using distance threshold and count #

def haversine_dist(lat1, lon1, lat2, lon2):
	"""Calculate the Haversine distance between two geo co-ordiantes."""
	radius = 3959  # miles
	dlat = math.radians(lat2 - lat1)
	dlon = math.radians(lon2 - lon1)
	a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
	d = radius * c
	return d

if __name__ == '__main__':
	df = pd.read_csv("../data/data-ny.csv", sep = ',', header=None, names =  ['userid', 'venueid', 'venuecatid', 'venuecatname','latitude','longitude','timezone','utctime'])
	category = "Coffee Shop"
	user = 642

	category_rows = get_rows_by_category(df, category)
	venue_group = get_checkin_count_per_venue_in_category(category_rows)
	count_venue = get_number_of_venues_per_category(venue_group)
	user_venue_group = get_sorted_user_checkin_count_at_venues(category_rows)
	count_user_venue = get_number_venues_visited_by_user(user_venue_group, user)
	user_rows = get_all_user_checkins(df, user)
	calculate_checkins_within_venue_radius(venue_group, user_rows)

