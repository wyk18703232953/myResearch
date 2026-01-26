import math
import sys
import collections
import bisect
import time
import random
from itertools import permutations
def get_ints():return map(int, sys.stdin.readline().strip().split())
def get_list():return list(map(int, sys.stdin.readline().strip().split()))
def get_string():return sys.stdin.readline().strip()
for t in range(1):
    n=int(input())
    arr=get_list()
    unique=set(arr)
    poss=False
    for i in arr:
        for j in range(32):
            if i+(2**j) in unique and i-(2**j) in unique:
                print(3)
                print(i,i+2**j,i-2**j)
                poss=True
                break
        if poss:
            break
    if poss:
        break
    for i in arr:
        for j in range(32):
            if i+(2**j) in unique:
                print(2)
                print(i,i+2**j)
                poss=True
                break
        if poss:
            break
    if poss:
        break
    print(1)
    print(arr[0])