from sys import stdin, stdout
from collections import defaultdict

n, m, k = map(int, stdin.readline().split())

dic = defaultdict(lambda : {})
for i in range(n):
    line = tuple(map(int, stdin.readline().split()))
    for j in range(m-1):
        dic[i*m+j][i*m+j+1] = line[j]*2
        dic[i*m+j+1][i*m+j] = line[j]*2

for i in range(n-1):
    line = tuple(map(int, stdin.readline().split()))
    for j in range(m):
        dic[i*m+j][(i+1)*m+j] = line[j]*2
        dic[(i+1)*m+j][i*m+j] = line[j]*2

if k % 2 != 0:
    for i in range(n):
        stdout.write(' '.join(('-1',)*m))
        stdout.write('\n')
else:
    prev = []
    di = (1, 0, -1, 0)
    dj = (0, 1, 0, -1)
    for _ in range(n):
        prev.append((0,)*m)

    for _ in range(k//2):
        new = []
        for _ in range(n):
            new.append([100_000_000]*m)

        for num in dic:
            i = num // m
            j = num % m
            for idx in range(4):
                ii = i + di[idx]
                jj = j + dj[idx]
                if not ((0 <= ii < n) and (0 <= jj < m)): continue
                new[ii][jj] = min(new[ii][jj], prev[i][j] + dic[i*m+j][ii*m+jj])

        prev = new
        
    for i in range(n):
        stdout.write(' '.join(map(str, prev[i])))
        stdout.write('\n')
                            
