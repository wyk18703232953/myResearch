import sys
input=sys.stdin.readline
n,k=map(int,input().split())
theorems=list(map(int,input().split()))
sleep=list(map(int,input().split()))
tsum=[]
ts=0
sleepsum=[]
slsum=0
for i in range(n):
    ts+=theorems[i]
    tsum.append(ts)
    if(sleep[i]==1):
        slsum+=theorems[i]
    sleepsum.append(slsum)
#print("tsum=",tsum)
#print("sleepsum=",sleepsum)
maxdiff=0
#print("slsum=",slsum)
maxdiff=tsum[k-1]-sleepsum[k-1]
for i in range(1,n-k+1):
    diff=(tsum[i+k-1]-tsum[i-1])-(sleepsum[i+k-1]-sleepsum[i-1])
    #print("i=",i,"diff=",diff)
    maxdiff=max(maxdiff,diff)
#print("maxdiff=",maxdiff)
print(slsum+maxdiff)