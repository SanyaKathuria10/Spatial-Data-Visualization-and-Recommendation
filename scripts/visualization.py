import matplotlib.pyplot as plt
import pandas as pd
# import plotly.plotly as py
# import plotly.graph_objs as go
from PIL import Image

im = Image.open('ny.png')
width, height = im.size
print(width)
print(height)

df = pd.read_csv("../data/data-ny.csv", sep = ',', header=None, names =  ['userid', 'venueid', 'venuecatid', 'venuecatname','latitude','longitude','timezone','utctime'])

# trace = go.Scatter(
#     x = df.latitute,
#     y = df.longitude,
#     mode = 'markers'
# )

# data = [trace]

py.iplot(data, filename = "Scatter Plot")

print(df[:10])
print(df.longitude[:10])

im = plt.imread("ny.png")
implot = plt.imshow(im)
ax = plt.subplot(1,1,1)
ax.set_ylim(40.5, 45.25)
ax.spines["bottom"].set_position('zero')
xlabel = ax.xaxis.get_label()
lpos = xlabel.get_position()
xlabel.set_position((1.04, lpos[1] De))
# put a blue dot at (10, 20)

# put a red dot, size 40, at 2 locations:


plt.scatter(x=df.latitude, y = df.longitude, c='r', s=40)

plt.show()

plt.scatter(x = df.latitude, y = df.longitude, alpha = 0.8)
plt.show()