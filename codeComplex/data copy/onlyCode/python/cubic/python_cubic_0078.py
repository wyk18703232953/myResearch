from math import log
import random
spaces = (" ","\n","\t")
stops = (""," ","\n","\t")
extendedPoints = set()
startingPoints = set()
interestPoints = []

class TPoint:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __str__(self):
		return "("+str(self.x)+","+str(self.y)+")"
	def __eq__(self, other): 
		return self.x == other.x and self.y == other.y
	def __hash__(self):
		return self.x*20000 + self.y
	x=0
	y=0
	h=0	# эвристика
def sortKey(p):
	return p.h
def heuristic(p, otherPoints):
	minH = float("inf")
	for point in otherPoints:
		currentH = abs(point.x - p.x) + abs(point.y - p.y)
		if currentH < minH:
			minH = currentH
	return minH

def addPoint(p,pointList):
	if not p in extendedPoints:
		p.h = heuristic(p,startingPoints)
		extendedPoints.add(p)
		pointList.append(p)
		#print(p.x,p.y,p.h)
		return True
	else:
		return False

def extend(point,n,m,poinList):
	ok = False
	if point.x>1:
		ok = addPoint(TPoint(point.x-1,point.y),poinList) or ok
		if point.y>1:
			ok = addPoint(TPoint(point.x-1,point.y-1),poinList) or ok
		if point.y<m:
			ok = addPoint(TPoint(point.x-1,point.y+1),poinList) or ok
	if point.x<n:
		ok = addPoint(TPoint(point.x+1,point.y),poinList) or ok
		if point.y>1:
			ok = addPoint(TPoint(point.x+1,point.y-1),poinList) or ok
		if point.y<m:
			ok = addPoint(TPoint(point.x+1,point.y+1),poinList) or ok
	if point.y>1:
		ok = addPoint(TPoint(point.x,point.y-1),poinList) or ok
	if point.y<m:
		ok = addPoint(TPoint(point.x,point.y+1),poinList) or ok

	return ok

def ReadNext(fileObject):
	currentBuffer = ""
	currentRead=fileObject.read(1)
	while currentRead in spaces:
		currentRead=fileObject.read(1)
	currentBuffer = currentBuffer + currentRead
	while not currentRead in stops:
		currentRead=fileObject.read(1)
		currentBuffer = currentBuffer + currentRead
	return currentBuffer.strip()

w, r= open('output.txt', 'w'), open('input.txt', 'r')

n = int(ReadNext(r))
m = int(ReadNext(r))
k = int(ReadNext(r))
mscale = 5

for i in range(k):
	x = int(ReadNext(r))
	y = int(ReadNext(r))
	p = TPoint(x,y)
	startingPoints.add(p)
	extendedPoints.add(p)

tmpPoints = []
tmpPoints.append(TPoint(1,1))
tmpPoints.append(TPoint(1,m))
tmpPoints.append(TPoint(n,1))
tmpPoints.append(TPoint(n,m))
if n>2 and m>2:
	tmpPoints.append(TPoint(int(n/2),1))
	tmpPoints.append(TPoint(1,int(m/2)))
	tmpPoints.append(TPoint(int(n/2),m))
	tmpPoints.append(TPoint(n,int(m/2)))
	tmpPoints.append(TPoint(int(n/2),int(m/2)))

for p in tmpPoints:
	addPoint(p,interestPoints)
	#extend(p,n,m,interestPoints)
for p in startingPoints:
	extend(p,n,m,interestPoints)

interestPoints.sort(reverse=True, key=sortKey)
while len(interestPoints) > 3*mscale:
	interestPoints.pop(len(interestPoints)-1)

random.seed()

if(len(interestPoints)>0):
	maxPoint = interestPoints[0]
	for p in interestPoints:
		currentBeam = [p]
		canExtend = True
		while canExtend:
			addPoint(TPoint(random.randint(1,n),random.randint(1,m)),currentBeam)
			canExtend = False
			for i in range(len(currentBeam)):
				if extend(currentBeam[i],n,m,currentBeam):
					canExtend = True
			currentBeam.sort(reverse=True, key=sortKey)
			while len(currentBeam) > mscale:
				currentBeam.pop(len(currentBeam)-1)
		if currentBeam[0].h>maxPoint.h:
			maxPoint = currentBeam[0]
	#print(maxPoint.x,maxPoint.y)
	#print(str(len(extendedPoints)))
	w.write(str(maxPoint.x)+" "+str(maxPoint.y)+"\n")
else:
	w.write(str(n)+" "+str(m)+"\n")
