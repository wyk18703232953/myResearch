import sys
from random import *
from bisect import *
from heapq import *
#from collections import deque
pl=1
from math import gcd,sqrt,ceil
from copy import *
sys.setrecursionlimit(10**5)
if pl:
	input=sys.stdin.readline
else:	
	sys.stdin=open('input.txt', 'r')
	sys.stdout=open('outpt.txt','w')

def li():
	return [int(xxx) for xxx in input().split()]
def fi():
	return int(input())
def si():
	return list(input().rstrip())	
def mi():
	return 	map(int,input().split())	

		
t=1

while t>0:
	t-=1
	s=input().rstrip()
	n=len(s)
	d={}
	for i in range(n):
		r=""
		for j in range(i,n):
			r+=s[j]
			if r not in d:
				d[r]=1
			else:
				d[r]+=1
	maxi=0			
	for i in d:
		if d[i]>=2:
			maxi=max(maxi,len(i))
	print(maxi)		
 	 		 		 	 				 		  	 		 	  			