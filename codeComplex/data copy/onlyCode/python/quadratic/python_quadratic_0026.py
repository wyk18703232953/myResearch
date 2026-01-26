import sys
from random import *
from bisect import *
#from collections import deque
pl=1
from math import gcd,sqrt
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
	n=fi()
	mod=10**9+7
	dp=[[0 for i in range(n+5)] for j in range(n+5)]
	prev="-1"
 
	for i in range(n):
		p=input().rstrip()
		if i==0:
			dp[i][0]=1
		else:
			
			c=0
			if prev=='f':
				for j in range(n):
					dp[i][j+1]=dp[i-1][j]
			else:	
				for j in range(n,-1,-1):
					c=(c+dp[i-1][j])%mod
					dp[i][j]=c	
				
		prev=p
	
	print(sum(dp[n-1])%mod)					
				