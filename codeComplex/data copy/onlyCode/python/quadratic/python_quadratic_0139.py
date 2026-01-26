n = int(input())
s = [["" for _ in range(n)] for __ in range(4)]
for i in range(3):
    for j in range(n):
        s[i][j] = input()
    input()
for j in range(n):
    s[3][j] = input()
res = int(1e13)
for i in range(24):
    perm = [0, 1, 2, 3]
    L = [0]*4
    tmp = i
    for j in range(4):
        L[j] = tmp % (4-j)
        tmp //= (4-j)
    LL = [0]*4
    for j in range(4):
        LL[j] = perm[L[j]]
        for k in range(L[j], 3-j):
            perm[k] = perm[k+1]
    lu, ru, ld, rd = LL[0], LL[1], LL[2], LL[3]
    Map = [s[lu][_][:]+s[ru][_][:] for _ in range(n)] + [s[ld][_][:]+s[rd][_][:] for _ in range(n)]
    cnt0, cnt1 = 0, 0
    for j in range(2*n):
        for k in range(2*n):
            if (j+k) % 2:
                if Map[j][k] == '0':
                    cnt0 += 1
                else:
                    cnt1 += 1
            else:
                if Map[j][k] == '1':
                    cnt0 += 1
                else:
                    cnt1 += 1
    res = min(res, cnt0, cnt1)
print(res)