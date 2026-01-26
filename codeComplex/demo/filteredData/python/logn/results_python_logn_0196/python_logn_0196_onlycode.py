import sys
input=sys.stdin.readline
n,s=map(int,input().split())
l=0;r=n+1
while r-l>1:
    x=(l+r)//2
    cs=0
    m=x
    while m>0:
        cs+=m%10
        m//=10
    if x-cs>=s:
        r=x
    else:
        l=x
print(n-l)