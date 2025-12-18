def BIG(NUM):
    X=NUM
    SM=0
    while X!=0:
        M=X%10
        SM+=M
        X//=10
    if NUM-SM>=S:
        return True

import sys
sys.setrecursionlimit(int(1e5))
input=sys.stdin.readline
N,S=map(int,input().split())
F=0;L=N+1;MN=1<<64
while L>=F:
    M=(L+F)>>1
    if BIG(M):L=M-1;MN=min(MN,M)
    else:F=M+1
if MN==1<<64:
    print(0)
else:
    print(N-MN+1)