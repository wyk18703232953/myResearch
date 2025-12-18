import sys
import io, os
import math
gcd=math.gcd
ceil=math.ceil
#arr=list(map(int, input().split()))
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
mod1=(10**9)+7
mod2=998244353
def strinp(testcases):
    k=5
    if(testcases==-1 or testcases==1):
        k=1
    f=str(input())
    f=f[2:len(f)-k]
    return f
def alp(a):
    return (ord(a)-ord("a"))
def main():
    arr=list(map(int, input().split()))
    n=arr[0]
    m=arr[1]
    k=arr[2]
    lrw=[0]*n
    for i in range(n):
        lrw[i]=list(map(int, input().split()))
    udw=[0]*(n-1)
    for i in range(n-1):
        udw[i]=list(map(int, input().split()))
    if(k%2==1):
        a=[-1]*m
        for i in range(n):
            print(*a)
        sys.exit()
    dp1=[[0 for i in range(m)] for j in range(n)]
    dp2=[[0 for i in range(m)] for j in range(n)]
    inf=10**10
    dis=(k//2)
    for h in range(dis):
        for i in range(n):
            for j in range(m):
                a=inf
                b=inf
                c=inf
                d=inf
                if(j>0):
                    a=lrw[i][j-1]+dp2[i][j-1]
                if(j<m-1):
                    b=lrw[i][j]+dp2[i][j+1]
                if(i>0):
                    c=udw[i-1][j]+dp2[i-1][j]
                if(i<n-1):
                    d=udw[i][j]+dp2[i+1][j]
                dp1[i][j]=min(a,b,c,d)
        dp2=dp1
        dp1=dp1=[[0 for a in range(m)] for b in range(n)]
    for i in range(n):
        for j in range(m):
            dp2[i][j]*=2
    for i in range(n):
        print(*dp2[i])
        
                
if __name__ == '__main__':
    main()