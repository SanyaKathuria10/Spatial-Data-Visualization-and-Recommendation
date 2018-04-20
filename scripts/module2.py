import pandas as pd
import math
from scipy.spatial import ConvexHull
import numpy as np



if __name__ == '__main__':
	df = pd.read_csv("../data/data-ny.csv", sep = ',', header=None, names =  ['userid', 'venueid', 'venuecatid', 'venuecatname','latitude','longitude','timezone','utctime'])
	category = "Coffee Shop"
	user = 642
	time = 16

