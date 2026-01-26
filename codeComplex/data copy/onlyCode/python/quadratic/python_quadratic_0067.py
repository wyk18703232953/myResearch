import sys
input=sys.stdin.readline
def getsum(BITTree,i):
    i=i+1
    s = 0
    while i > 0:
        s += BITTree[i]
        i -= i & (-i) 
    return(s) 
def updatebit(BITTree , n , i ,v):
    i=i+1
    while i <= n:
        BITTree[i] += v
        i += i & (-i)
    #print(BITTree)
n=int(input())
lista=[int(i) for i in input().split()]
invercount=0
bitTree=[0]*(n+2)
for k in reversed(lista):
        updatebit(bitTree,n+1,k,1)
        counter=getsum(bitTree,k-1)
        invercount+=counter
m=int(input())
for i in range(m):
    l,r=map(int,input().split())
    summa=((r-l+1)*(r-l))/2
    if (invercount+summa)%2:
        print('odd')
        invercount=1
    else:
        print('even')
        invercount=0
    
