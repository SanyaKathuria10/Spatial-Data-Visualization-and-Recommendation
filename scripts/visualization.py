import matplotlib.pyplot as plt
import pandas as pd
# import plotly.plotly as py
# import plotly.graph_objs as go

df = pd.read_csv("../data/data-ny.csv", sep = ',', header=None, names =  ['userid', 'venueid', 'venuecatid', 'venuecatname','latitute','longitude','timezone','utctime'])

# trace = go.Scatter(
#     x = df.latitute,
#     y = df.longitude,
#     mode = 'markers'
# )

# data = [trace]

# py.iplot(data, filename = "Scatter Plot")

# print(df[:10])
# print(df.longitude[:10])

plt.scatter(x = df.latitute, y = df.longitude, alpha = 0.8)
plt.show()