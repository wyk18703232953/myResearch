import math,sys,bisect,heapq,os
from collections import defaultdict,Counter,deque
from itertools import groupby,accumulate
from functools import lru_cache
#sys.setrecursionlimit(200000000)
int1 = lambda x: int(x) - 1
def input(): return sys.stdin.readline().rstrip('\r\n')
#input = iter(sys.stdin.buffer.read().decode().splitlines()).__next__
aj = lambda: list(map(int, input().split()))
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
#MOD = 1000000000 + 7
def Y(c):  print(["NO","YES"][c])
def y(c):  print(["no","yes"][c])
def Yy(c):  print(["No","Yes"][c])



def solve():
	G = defaultdict(list)

	def addEdge(a,b):
		G[a].append(b)

	def Kahn(N):
	    in_degree = [0]*(N+1)
	    for i in G.keys():
	        for j in G[i]:
	            in_degree[j] += 1
	    queue = deque()
	    for i in range(1,N+1):
	        if in_degree[i] == 0:
	            queue.append(i)
	    cnt =0
	    top_order = []
	    while queue:
	        u = queue.popleft()
	        top_order.append(u)
	        for i in G.get(u,[]):
	            in_degree[i] -= 1
	            if in_degree[i] == 0:
	                queue.append(i)
	        cnt += 1
	    if cnt != N:
	        Y(0);exit(0)
	    else:
	        Y(1);print(*top_order)

	n,m,k = aj()
	mark= {}
	for i in range(n):
		s = input()
		mark[s] = i+1

	B = []
	for i in range(2**k):
		f = bin(i)[2:]
		f = '0'*(k - len(f)) + f
		B.append(f)

	for i in range(m):
		s,mt = input().split(" ")
		mt = int(mt)
		st = set()
		for j in B:
			ss = ['']*k
			for l in range(k):
				if j[l] == '1':
					ss[l] = s[l]
				else:
					ss[l] = '_'
			ss = "".join(ss)
			if ss in mark:
				st.add(mark[ss])
		#print(st)
		if mt not in st:
			Y(0);exit(0)
		st.discard(mt)
		for j in st:
			addEdge(mt,j)
	#print(G)
	Kahn(n)


try:
	#os.system("online_judge.py")
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')
except:
	pass

solve()