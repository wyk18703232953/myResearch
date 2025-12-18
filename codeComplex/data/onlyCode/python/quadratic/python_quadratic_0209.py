import sys
import io, os
input = sys.stdin.readline

n, m = map(int, input().split())
A = [input().rstrip() for i in range(n)]
C = [0]*m
for i in range(n):
    a = A[i]
    for j, c in enumerate(a):
        C[j] += int(c)

for i in range(n):
    a = A[i]
    for j, c in enumerate(a):
        C[j] -= int(c)
    for j in range(m):
        if C[j] == 0:
            break
    else:
        print('YES')
        exit()
        continue
    for j, c in enumerate(a):
        C[j] += int(c)
print('NO')
