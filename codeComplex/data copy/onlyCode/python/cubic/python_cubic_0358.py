import os
import io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline 
 
from math import sqrt,ceil
 
max_n=10**7+1
spf = [i for i in range(max_n)]
 
for i in range(4,max_n,2): 
    spf[i]=2
    
for i in range(3,ceil(sqrt(max_n))): 
    if (spf[i]==i):  
        for j in range(i*i,max_n,i):  
            if(spf[j]==j):
                spf[j]=i
                
from collections import Counter,defaultdict
from bisect import insort
 
def f(x):
    c=Counter()
    ans=1
    while(x!=1):
        c[spf[x]]+=1
        x//=spf[x] 
    for i in c:
        if(c[i]%2==1):
            ans*=i
    return(ans)
 
#https://www.geeksforgeeks.org/prime-factorization-using-sieve-olog-n-multiple-queries/
 
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(n):
        a[i]=f(a[i])
    dp_depth=[[n for j in range(k+1)] for i in range(n)] #Maximum length that can be tranversed in list, starting from index i with atmost j repeated elements(default is entire length of list(max possible)
    recent=[n for i in range(k+1)] #Stores position of most recent repeated element in the suffix(default is one more that maximum index(when no sufficient repeats))
    closest=defaultdict(lambda: -1) #Stores index of first repetition for a particular ai 
    for i in range(n-1,-1,-1):
        if(closest[a[i]]>=0):
            insort(recent,closest[a[i]])
            recent.pop()
        dp_depth[i]=recent.copy()
        closest[a[i]]=i 
    dp=[[i for j in range(k+1)] for i in range(n+1)]
    #dp=[[float('inf') for j in range(k+1)] for i in range(n+1)] #Minimum number of sets in the prefix segment upto(and **excluding**) index i after atmost k changes(which is also = number of partitions/splits(number of element changes) upto and **excluding** index i).
    #Note we could have changed the float('inf') to "i" but that's tougher to debug.
    dp[0]=[0 for j in range(k+1)] #base case(don't need to divide at all before element at index 0(first element))
    for i in range(n):
        for x in range(k+1): 
            end=dp_depth[i][x] #The end point of our segment(upto and exluding this index position)
            #We are dividing each segment into subsegments: prefix consisting of [0,i), suffix consisting from [i,end)
            #x is the number of partitions/splits(number of elements we change) in the suffix subsegment(Number of repeated elements starting from index i)
            for y in range(k-x+1): #y is the number of partitions/splits(number of elements we change) in the prefix subsegment
                dp[end][x+y]=min(dp[end][x+y],dp[i][y]+1) #after using the previously calculated value dp[i][y](<=y changes), with <= x more "changes"(equality holds iff end=n) in the suffix segment, this gives an extra set starting from [i,end). So overall, we get number of sets of dp[i][y]+1.
    print(dp[n][k])
                
                
            

