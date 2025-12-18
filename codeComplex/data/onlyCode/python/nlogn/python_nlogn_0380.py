from sys import stdin,stdout
import heapq
nmbr=lambda:int(stdin.readline())
lst=lambda:list(map(int,stdin.readline().split()))
for _ in range(1):#nmbr()):
    n,k=lst()
    l=sorted(zip(lst(),lst(),range(n)))
    h=[];sm=0
    ans={}
    for i in range(n):
        pwr,cns,ind=l[i]
        sm+=cns
        if len(h)>k:
            sm-=heapq.heappop(h)
        ans[ind]=sm
        heapq.heappush(h,cns)
    for i in range(n):
        stdout.write(str(ans[i])+' ')
    print()