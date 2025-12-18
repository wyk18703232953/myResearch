import bisect
import collections
import copy
import functools
import heapq
import itertools
import math
import random
import re
import sys
import time
import string
from time import time_ns
from typing import List
sys.setrecursionlimit(99999)

def II():return int(sys.stdin.readline().strip())
def IIs():return list(map(int,sys.stdin.readline().strip().split()))
def SI():return sys.stdin.readline().strip()

n=II()
if n&1:
    print(9,n-9)
else:
    print(8,n-8)