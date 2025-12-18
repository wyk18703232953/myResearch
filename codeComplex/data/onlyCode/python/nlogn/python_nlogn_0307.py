
# Problem: B. Bus of Characters
# Contest: Codeforces - Codeforces Round #484 (Div. 2)
# URL: https://codeforces.com/contest/982/problem/B
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# Powered by CP Editor (https://github.com/cpeditor/cpeditor)

from sys import stdin
def get_ints(): return list(map(int, stdin.readline().strip().split()))

n = int(input())
ar = get_ints()

bus = sorted([ (ar[i], i+1) for i in range(n) ])
pa = [int(x) for x in input()]
seq = []
# print(bus)
tail = 0
for p in pa:
	if p == 0:
		print(bus[tail][1], end=" ")
		seq.append(tail)
		tail+=1
	else:
		v = seq.pop()
		print(bus[v][1],end=" ")
