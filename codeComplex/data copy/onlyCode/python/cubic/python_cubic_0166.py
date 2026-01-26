from heapq import *
import sys

int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    inf=10**9
    n=II()
    aa=LI()
    dp1=[[-1]*(n+1) for _ in range(n)]
    to=[[i+1] for i in range(n)]
    for i in range(n):dp1[i][i+1]=aa[i]
    for w in range(2,n+1):
        for l in range(n-w+1):
            r=l+w
            for m in range(l+1,r):
                if dp1[l][m]!=-1 and dp1[l][m]==dp1[m][r]:
                    dp1[l][r]=dp1[l][m]+1
                    to[l].append(r)
    hp=[]
    heappush(hp,(0,0))
    dist=[-1]*(n+1)
    while hp:
        d,i=heappop(hp)
        if i==n:
            print(d)
            break
        if dist[i]!=-1:continue
        dist[i]=d
        for j in to[i]:
            if dist[j]!=-1:continue
            heappush(hp,(d+1,j))

main()