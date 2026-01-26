import sys
from itertools import chain, combinations

def powerset(iterable):
	s = list(iterable)
	return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def diff(s, x):
	return True if (max(s)-min(s))>=x else False

def solve(problemset, l, r, x):
	multiset = powerset(problemset)
	cnt = 0
	for s in multiset:
		if sum(s)>=l and sum(s)<=r and diff(s, x):
			cnt += 1
	return cnt


sys.setrecursionlimit(10**7)

def I(): return int(sys.stdin.readline().rstrip())
def MI():return map(int, sys.stdin.readline().rstrip().split())
def LI():return list(map(int, sys.stdin.readline().rstrip().split()))
def LI2():return list(map(int, sys.stdin.readline().rstrip()))
def S():return sys.stdin.readline().rstrip()
def LS():return list(sys.stdin.readline().rstrip().split())
def LS2():return list(sys.stdin.readline().rstrip())

n, l, r, x = MI()

problemset = LI()

print(solve(problemset, l, r, x))