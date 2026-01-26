from math import sqrt

def inpl():
	return list(map(int, input().split()))

def inpi():
	return int(input())

def issq(p):
	x = int(sqrt(p))
	return x*x == p

def g(n):
	return (issq(n//2) and n%2==0) or (issq(n//4) and n%4==0)

def f():
	n = inpi()

	print("YES" if g(n) else "NO")

t = int(input())
for _ in range(t):
	f()
