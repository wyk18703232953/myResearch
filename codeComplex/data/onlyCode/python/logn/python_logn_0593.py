import sys
def ints():
    return list(map(int, sys.stdin.readline().strip().split()))
tc = 1#int(input())
while tc:
    tc-=1
    n, k = map(int, input().split())
    l = -1
    r = n+1
    while r-l > 1:
        m = (r+l)//2
        if (n-m)*(n-m+1)//2 - m > k:
            l = m
        else:
            r = m
    print(r)