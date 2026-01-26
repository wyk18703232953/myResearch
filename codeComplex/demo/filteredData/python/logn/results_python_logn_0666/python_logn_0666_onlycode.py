from collections import defaultdict as dd, deque as dq
import math, string

import sys

def getInts():
    return [int(s) for s in input().split()]

def getInt():
    return int(input())

def getStrs():
    return [s for s in input().split()]

def getStr():
    return input()

def listStr():
    return list(input())

MOD = 10**9+7

"""
x*(x+1)//2 candies were placed in the box
N-x candies were eaten
K candies remain
x*(x+1)//2 + x - N - K = 0
x**2 +3*x - 2*(N + K) = 0
x = (-3 + sqrt(9+4*(N+K)))*0.5
"""

def solve():
    N, K = getInts()
    x = (-3 + math.sqrt(9+8*(N+K)))//2
    return int(x*(x+1)//2 - K)
    
    
#for _ in range(getInt()):
print(solve())