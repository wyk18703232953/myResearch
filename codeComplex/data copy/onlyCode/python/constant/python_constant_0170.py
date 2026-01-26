import sys, collections, math, itertools, random, bisect
INF = sys.maxsize
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def input(): return sys.stdin.readline().strip()
mod = 1000000007

l,r = get_ints()
if r-l < 2:
    print(-1)
elif l%2 == 0:
    print(l, l+1, l+2)
elif r-l > 2:
    print(l+1, l+2, l+3)
else:
    print(-1)