# Foursquare NYC Check-In Visualization and Recommendation Engine 
Spatial Temporal Data Mining Project Spring 2018

In this project, we investigate the Foursquare checkins dataset containing 227,428 check-ins in New York city and report an assessment of human mobility patterns by analyzing the spatial and temporal aspects associated with these footprints. We attempt to explore the behaviours of users in New York city and then visualize the dataset to find interesting patterns. We then present a recommender system which suggests a particular set of venues (such as restaurants) to a user and then further also develop a second model for recommending a set of users to a venue, keeping in mind both user-preferences, users’ location and popularity of the venues. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites
You need to have Python versions 2.x or later to run this project.

### Installing

The following python libraries need to be installed:
1. pandas
2. scipy
3. numpy
4. sklearn
5. gmplot
6. matplotlib
7. webbrowser

If you are using pip then run the following commands:
```
pip install pandas
pip install scipy
pip install numpy
pip install sklearn
pip install gmplot
pip install matplotlib
pip install webbrowser

```

###Running the modules

##Module 1: Visualization using Heat Map

```

python visualization-gmap.py

```

##Module 2: Recommending places to users

```
python recom.py <category name> <userid> <current time in hrs>

For eg: python recom.py "Coffee Shop" 642 16

```

##Module 3: Recommending users to places

## Authors

* **Neel Kapadia** - [neelkapadia](https://github.com/neelkapadia)
* **Tushita Roychaudhury** - [tushitarc](https://github.com/tushitarc)
* **Sanya Kathuria** - [SanyaKathuria10](https://github.com/SanyaKathuria10)


## Acknowledgments

* We thank our instructors, Dr. Raju Vatsavai and TA Bharathkumar Ramachandra, for their support throughout the project

