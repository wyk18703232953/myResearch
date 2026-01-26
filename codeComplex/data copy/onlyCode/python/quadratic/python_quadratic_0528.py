import math as ma
import sys
from sys import exit
from decimal import Decimal as dec
from itertools import permutations


def li():
	return list(map(int , input().split()))


# https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
def modInverse(a , m):
	m0 = m
	y = 0
	x = 1
	if (m == 1):
		return 0
	while (a > 1):
		q = a // m
		t = m
		m = a % m
		a = t
		t = y
		y = x - q * y
		x = t
	if (x < 0):
		x = x + m0
	return x


def num():
	return map(int , input().split())


def nu():
	return int(input())


def find_gcd(x , y):
	while (y):
		x , y = y , x % y
	return x

n,m=num()
a=[0]*n
for i in range(n):
	a[i]=[0]*m
for i in range(n):
	s=input()
	for j in range(m):
		a[i][j]=s[j]
z=["."]*n
for i in range(n):
	z[i]=["."]*m
for i in range(n):
	for j in range(m):
		if(j-1>=0 and j+1 <m and i+1<n and i-1>=0):
			if(a[i-1][j]=="#" and a[i+1][j]=="#" and a[i][j-1]=="#" and a[i][j+1]=="#" and a[i-1][j-1]=="#" and a[i-1][j+1]=="#" and a[i+1][j-1]=="#" and a[i+1][j+1]=="#"):
				z[i-1][j]="#"
				z[i + 1][j] = "#"
				z[i][j - 1] = "#"
				z[i][j + 1] = "#"
				z[i - 1][j - 1] = "#"
				z[i - 1][j + 1] = "#"
				z[i + 1][j - 1] = "#"
				z[i + 1][j + 1] = "#"
ff=True

for i in range(n):
	for j in range(m):
		if(z[i][j]!=a[i][j]):
			ff=False
			break
if(ff):
	print("YES")
else:
	print("NO")