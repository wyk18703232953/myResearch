import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int, readline().split()))
Q = int(readline())

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        if A[i] > A[j]:
            cnt += 1

cnt %= 2

Ans = [None]*Q
for qu in range(Q):
    l, r = map(int, readline().split())
    if (r-l+1)*(r-l)//2 & 1:
        cnt ^= 1
    
    Ans[qu] = 'odd' if cnt else 'even'

print('\n'.join(Ans))