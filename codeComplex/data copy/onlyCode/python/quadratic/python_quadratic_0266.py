n, a, b = map(int, input().strip().split())

if min(a, b) > 1:
    print('NO')
    exit(0)

M = [[0] * n for _ in range(n)]

if a == 1 and b == 1:
    if n == 1:
        print('YES')
        print('0')
        exit(0)
    if n == 2 or n == 3:
        print('NO')
        exit(0)    
    for i in range(1, n):
        M[i - 1][i] = 1
        M[i][i - 1] = 1    
else:
    # assume b == 1
    s = n - max(a, b) + 1
    for i in range(s):
        for j in range(s):
            if i != j:
                M[i][j] = 1
    if a == 1:
        for i in range(n):
            for j in range(n):
                if i != j:
                    M[i][j] = 1 - M[i][j]

print('YES')
for i in range(n):
    print(''.join(map(str, M[i])))