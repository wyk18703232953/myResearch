
from sys import stdin,stdout,setrecursionlimit
stdin.readline
def mp(): return list(map(int, stdin.readline().strip().split()))
def it():return int(stdin.readline().strip())
from collections import defaultdict as dd,Counter as C,deque
from math import ceil,gcd,sqrt,factorial,log2,floor	
from bisect import bisect_right as br,bisect_left as bl
import heapq

def solve(a,b):
	if a == 0:
		return 0
	return b//a + solve(b%a,a)
print(solve(*mp()))

