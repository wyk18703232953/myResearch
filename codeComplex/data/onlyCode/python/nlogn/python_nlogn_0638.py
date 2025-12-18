import sys
from math import *

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return map(int, minp().split())

def main():
	n,m = mints()
	vert = []
	horiz = []
	for i in range(n):
		x = mint()
		vert.append(x)

	vert.sort()

	for i in range(m):
		x1,x2,y = mints()
		horiz.append((y,x1,x2))

	horiz.sort()

	p = -1
	hh = []
	for i in horiz:
		if p != i[0]:
			p = i[0]
			if i[1] == 1:
				hh.append(i[2])

	hh.sort()
	i = 0
	hl = len(hh)
	vl = len(vert)
	r = n + m
	for j in range(vl):
		while i < hl and hh[i] < vert[j]:
			i+=1
		r = min(r, hl-i + j)
	while i < hl and hh[i] < 1000000000:
		i+=1
	r = min(r, hl-i + vl)
	print(r)

main()