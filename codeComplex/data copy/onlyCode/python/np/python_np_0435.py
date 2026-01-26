import sys
input = sys.stdin.readline

N, M = map(int, input().split())
state = [list(map(int, input().split())) for _ in range(N)]

Ans = {}

l = -1
r = 10**9+1
while r-l > 1:
    m = (l+r)//2
    T = {}
    for j, S in enumerate(state):
        bit = 0
        for i, s in enumerate(S):
            if s >= m:
                bit += 1<<i
        T[bit] = j
    
    ok = False
    for bit1 in range(1<<M):
        for bit2 in range(1<<M):
            if bit1|bit2 == (1<<M)-1 and bit1 in T and bit2 in T:
                ok = True
                Ans[m] = [T[bit1], T[bit2]]
                break
        if ok: break
    if ok:
        l = m
    else:
        r = m
print(Ans[l][0]+1, Ans[l][1]+1)