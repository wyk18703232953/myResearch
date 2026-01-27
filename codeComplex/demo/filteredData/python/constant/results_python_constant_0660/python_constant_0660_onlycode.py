l = []
a, b = map(int, input().split())
l.append((a,b))
a, b = map(int, input().split())
l.append((a,b))
a, b = map(int, input().split())
l.append((a,b))
l.sort()
path = []
path.append(l[0])
x = l[0][0]
while(x<l[1][0]):
	path.append((x, l[0][1]))
	x = x + 1
up = False
if(l[0][1]<l[1][1]):
	#print("why")
	up = True
if(up):
	y = l[0][1]
	while(y<=l[1][1]):
		path.append((l[1][0], y))
		y = y+1
else:
	y = l[0][1]
	while(y>=l[1][1]):
		path.append((l[1][0], y))
		y = y-1
up = False
if(l[1][1]<l[2][1]):
	up = True
if(up):
	y = l[1][1]
	while(y<=l[2][1]):
		path.append((l[1][0], y))
		y = y+1
else:
	y = l[1][1]
	while(y>=l[2][1]):
		path.append((l[1][0], y))
		y = y-1
x = l[1][0]
while(x<l[2][0]):
	path.append((x, l[2][1]))
	x = x + 1
path.append(l[2])
path = list(set(path))
print(len(path))
for i in range(len(path)):
	print(str(path[i][0])+" "+str(path[i][1]))

