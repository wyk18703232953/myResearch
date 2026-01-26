import sys
import math
from collections import OrderedDict
def input():    return sys.stdin.readline().strip()
def iinput():   return int(input())
def minput():   return map(int, input().split()) 
def listinput(): return list(map(int, input().split()))
n,k=minput()
if n==k:print(math.ceil(n/2)-1)
elif k>2*n:print(0)
else:print(min(n,k-1)-k//2)