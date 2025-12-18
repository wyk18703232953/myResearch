import sys
import math
from collections import OrderedDict
def input():    return sys.stdin.readline().strip()
def iinput():   return int(input())
def minput():   return map(int, input().split()) 
def listinput(): return list(map(int, input().split()))
n,k=minput()
for i in range(1,n+1):
	if (i*(i+1))/2 -n+i==k:
		print(n-i)
		break