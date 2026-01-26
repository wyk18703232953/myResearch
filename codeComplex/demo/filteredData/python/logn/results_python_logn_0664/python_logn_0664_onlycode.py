import sys     
import math as mt
import bisect
input=sys.stdin.readline
#t=int(input())
t=1
def ncr_util():
    inv[0]=inv[1]=1
    fact[0]=fact[1]=1
    for i in range(2,300001):
        inv[i]=(inv[i%p]*(p-p//i))%p
    for i in range(1,300001):
        inv[i]=(inv[i-1]*inv[i])%p
        fact[i]=(fact[i-1]*i)%p
def solve():
    a=1
    b=2*n+3
    c=n+n**2-2*k
    x1=b+int(mt.sqrt(b**2-4*a*c))
    x2=b-int(mt.sqrt(b**2-4*a*c))
    if x1%2==0 and x1//2<=n:
        return x1//2
    return x2//2    
        
    
for _ in range(t):
    #n=int(input())
    #n1=int(input())
    #s=input()
    #n=int(input())
    n,k=(map(int,input().split()))
    #n1=n
    #a=int(input())
    #b=int(input())
    #a,b,c,r=map(int,input().split())
    #x2,y2=map(int,input().split())
    #n=int(input())
    #s=input()
    #s1=input()
    #p=input()
    #l=list(map(int,input().split()))
    #l=str(n)
    #l.sort(reverse=True)
    #l2.sort(reverse=True)
    #l1.sort(reverse=True)
    print(solve())            
        