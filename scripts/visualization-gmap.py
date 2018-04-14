from gmplot import gmplot
import matplotlib.pyplot as plt
import pandas as pd
# Place map
gmap = gmplot.GoogleMapPlotter(40.7589, -73.9851, 9)
df = pd.read_csv("../data/data-ny.csv", sep = ',', header=None, names =  ['userid', 'venueid', 'venuecatid', 'venuecatname','latitute','longitude','timezone','utctime'])


# gmap = gmplot.GoogleMapPlotter.from_geocode("New York")

# Polygon
# golden_gate_park_lats, golden_gate_park_lons = zip(*[
#     (37.771269, -122.511015),
#     (37.773495, -122.464830),
#     (37.774797, -122.454538),
#     (37.771988, -122.454018),
#     (37.773646, -122.440979),
#     (37.772742, -122.440797),
#     (37.771096, -122.453889),
#     (37.768669, -122.453518),
#     (37.766227, -122.460213),
#     (37.764028, -122.510347),
#     (37.771269, -122.511015)
#     ])
# gmap.plot(golden_gate_park_lats, golden_gate_park_lons, 'cornflowerblue', edge_width=10)

# Scatter points
# top_attraction_lats, top_attraction_lons = zip(*[
#     (37.769901, -122.498331),
#     (37.768645, -122.475328),
#     (37.771478, -122.468677),
#     (37.769867, -122.466102),
#     (37.767187, -122.467496),
#     (37.770104, -122.470436)
#     ])
# print(type(top_attraction_lats))
# df= df[0:100]

tup_lat = list(df.latitute)
tup_long = list(df.longitude)


for x in range(len(tup_lat)):
	tup_lat[x] = float(tup_lat[x])

# print(tup_lat)

tup_lat = tuple(tup_lat)
tup_long = tuple(tup_long)

# Scatterplot
# gmap.scatter(tup_lat, tup_long, '#3B0B39', size=40, marker=False)
# Heatmap
gmap.heatmap(tup_lat, tup_long)

# print(type(tuple(df.latitute)))

# Marker
# hidden_gem_lat, hidden_gem_lon = 37.770776, -122.461689
# gmap.marker(tuple(df.latitute), tuple(df.longitude), 'cornflowerblue')

# Draw
gmap.draw("ny_heat_map.html")
