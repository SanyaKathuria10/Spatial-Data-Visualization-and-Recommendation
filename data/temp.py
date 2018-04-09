import re
line = "Hi   This is       Neel"

for i in range(1,len(line)):
	if line[i]==' ':
		if line[i-1]==' ':
			line = line[:i-1] + '_' + line[i:]
			while line[i]==' ':
				line = line[:i] + '_' + line[i + 1:]
				i = i + 1

line = re.sub(r'_*_', ',',line)
#line.replace(_*,',')
print(line)