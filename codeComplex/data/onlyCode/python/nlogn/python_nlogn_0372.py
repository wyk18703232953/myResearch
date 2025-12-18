from sys import stdin
from collections import deque,Counter
import sys
import math
import operator
import random
from fractions import Fraction

n,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
f = arr[0]
p = n
i = 0
count = 0
while i<n:
    while i<n and arr[i] == f:
        i+=1
        count+=1
    if i<n and arr[i]<=f+k:
        p-=count
    if i<n:
        f=arr[i]
        count=0
    continue

print(p)
