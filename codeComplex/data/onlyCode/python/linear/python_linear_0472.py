import sys
import io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

n = int(input())
C = list(map(int, input().split()))
A = list(map(int, input().split()))
A = [a-1 for a in A]

visit = [False]*n
loops = []
for i in range(n):
    if not visit[i]:
        s = [i]
        temp = set()
        temp.add(i)
        flag = False
        while s:
            v = s.pop()
            if visit[A[v]]:
                break
            if A[v] in temp:
                flag = True
                p = A[v]
                break
            else:
                s.append(A[v])
                temp.add(A[v])
        if flag:
            loop = [p]
            nv = A[p]
            cnt = 0
            while nv != p:
                loop.append(nv)
                nv = A[nv]
            loops.append(loop)
        for v in temp:
            visit[v] = True
#print(loops)
ans = 0
for l in loops:
    m = 10**18
    for i in l:
        m = min(m, C[i])
    ans += m
print(ans)
