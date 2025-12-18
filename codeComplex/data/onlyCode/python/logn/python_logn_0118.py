import bisect
import sys
input=sys.stdin.readline
#t=int(input())
import collections 
import heapq
t=1
p=10**9+7
def ncr_util():
    
    inv[0]=inv[1]=1
    fact[0]=fact[1]=1
    for i in range(2,300001):
        inv[i]=(inv[i%p]*(p-p//i))%p
    for i in range(1,300001):
        inv[i]=(inv[i-1]*inv[i])%p
        fact[i]=(fact[i-1]*i)%p

    
def solve():
    ans,a,b=0,0,0
    mul=2**60
    for i in range(60,-1,-1):
        #print(11,mul,a+mul,b+mul)
        ch1,ch2=0,0
        if a+mul<=l:
            #print(1,a,mul)
            a+=mul
            ch1=1
        if  b+mul<=l:
            #print(2,b,mul)
            b+=mul
            ch2=1
        if ch1^ch2==1:   
            ans+=mul
        elif ch1==0 and ch2==0:
            if a+mul<=r:
                a+=mul
                ans+=mul
            elif b+mul<=r:
                b+=mul
                ans+=mul
            #print(123,ans)
        mul//=2
    #print(a,b,a^b)
    return ans
     
    
for _ in range(t):
    #n=int(input())
    #s=input()
    #n=int(input())
    #h,n=(map(int,input().split()))
    #n1=n
    #x=int(input())
    #b=int(input())
    #n,m,k=map(int,input().split())
        
    #l=list(map(int,input().split()))
    l,r=map(int,input().split())
    #n=int(input())
    #s=input()
    #s1=input()
    #p=input()
    #l=list(map(int,input().split()))
    #l.sort(revrese=True)
    #l2=list(map(int,input().split()))
    #l=str(n)
    #l.sort(reverse=True)
    #l2.sort(reverse=True)
    #l1.sort(reverse=True)
    print(solve())
            
        