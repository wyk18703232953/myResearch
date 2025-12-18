# // "Author : Chinmay Jha
# // @chinmayajha on Codeforces, Codechef, AtCoder, USACO, CSES.fi
# // 
# // Problem: B. Businessmen Problems
# // Contest: Codeforces - Avito Code Challenge 2018
# // URL: https://codeforces.com/problemset/problem/981/B
# // Date / Time: 15-04-2021 20:39:59"
# 
import math
from math import gcd,floor,sqrt,log
def iin(): return int(input())
def sin(): return input().strip()
def listin(): return list(map(int,input().strip().split()))
def liststr(): return list(map(str,input().strip().split()))
def ceill(x): return  int(x) if(x==int(x)) else int(x)+1
def ceilldiv(x,d): x//d if(x%d==0) else x//d+1
def LCM(a,b): return (a*b)//gcd(a,b)


def solve():
	n = iin()
	cf = dict()
	tc = dict()
	for i in range(n):
		z = listin()
		cf[z[0]] = z[1]
	m = iin()	
	for i in range(m):
		z = listin()
		tc[z[0]] = z[1]
	# print(cf)
	# print(tc)
	sett = set(list(cf.keys()) + list(tc.keys()))
	# print(sett)
	summ = 0
	for i in sett:
		temp = 0
		try:
			temp = max(tc[i],cf[i])
		except:
			try:
				temp = cf[i]
			except:
				temp = tc[i]
		summ += temp
	print(summ)
		





t = 1 
# t = int(input()) 
for hula in range(t):
	solve()


