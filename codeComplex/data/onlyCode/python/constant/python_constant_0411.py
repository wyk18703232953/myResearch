import sys

def sol(a,b):
	for square in [a,b]:
		for i1 in range(4):
			i2 = (i1 + 1)%4
			p1,p2 = square[i1],square[i2]
			
			norm = (p2[1]-p1[1],p1[0]-p2[0])

			minA = maxA = minB = maxB = None
			for p in a:
				proj = norm[0] * p[0] + norm[1] * p[1]
				if minA == None or proj < minA:
					minA = proj
				if maxA == None or proj > maxA:
					maxA = proj
			for p in b:
				proj = norm[0] * p[0] + norm[1] * p[1]
				if minB == None or proj < minB:
					minB = proj
				if maxB == None or proj > maxB:
					maxB = proj

			if maxA < minB or maxB < minA:
				return False
	return True

x11,y11,x12,y12,x13,y13,x14,y14 = list(map(int,sys.stdin.readline().strip().split(' ')))
x21,y21,x22,y22,x23,y23,x24,y24 = list(map(int,sys.stdin.readline().strip().split(' ')))

a = [(x11,y11), (x12,y12), (x13,y13), (x14,y14)]
b = [(x21,y21), (x22,y22), (x23,y23), (x24,y24)]

print(["NO","YES"][sol(a,b)])