import pandas as pd
import re
from io import StringIO
#data = pd.read_csv("dataset_TSMC2014_NYC.txt", sep = " ", header=None, error_bad_lines=False)

df = pd.DataFrame(columns=['userid', 'venueid', 'venuecatid', 'venuecatname','latitute','longitude','timezone','utctime'])

content = open("dataset_TSMC2014_NYC.txt", encoding='latin-1')
content = list(content)

#print(type(content))
#print(content[0])
#x = ["470	 49bbd6c0f964a520f4531fe3	4bf58dd8d48988d127951735	Arts & Crafts Store	40.719810375488535	-74.00258103213994	-240	Tue Apr 03 18:00:09 +0000 2012"]
#x[0] = x[0].replace("\t", "   ")
f = open('data.csv', 'w')
#f.write('hi there\n')  # python will convert \n to os.linesep
#f.close()  # you can omit in most cases as the destructor will call it
count = 0
for line in content:
		line = line.replace("\t", "   ")
		for i in range(1,len(line)):
			if line[i]==' ':
				if line[i-1]==' ':
					line = line[:i-1] + '_' + line[i:]
					while line[i]==' ':
						line = line[:i] + '_' + line[i + 1:]
						i = i + 1
		#print(line)
		line = re.sub(r'_*_', ',',line)
		#print(line)
		#temp = pd.DataFrame([line.split(',')], columns = ['userid', 'venueid', 'venuecatid', 'venuecatname','latitute','longitude','timezone','utctime'])
		test = StringIO(line)
		f.write(test + "\n")
		#temp = pd.read_csv(test, sep = ',', header = None, names =  ['userid', 'venueid', 'venuecatid', 'venuecatname','latitute','longitude','timezone','utctime'])
		#print(temp)
		#temp = pd.DataFrame(temp)
		#print(temp)
		#temp = [df, temp]
		#df = df.merge(temp, on = ['userid', 'venueid', 'venuecatid', 'venuecatname','latitute','longitude','timezone','utctime'], how = 'left' )
		#df = pd.concat(temp)
		#count = count + 1

f.close()
#print(df)