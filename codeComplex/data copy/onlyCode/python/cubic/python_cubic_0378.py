n, mod = map(int, input().split())

le = 500


def pow(x, y):  # x**y の mod を返す。modは素数でなくてもよい。
    ans = 1
    while y > 0:
        if y % 2 == 1:
            ans = (ans * x) % mod
        x = (x**2) % mod
        y //= 2
    return ans


def inv(x):  # x の mod での逆元を返す。modが素数で、xとmodが互いに素である必要あり。
    return pow(x, mod-2)


M = [1]  # i!のmod
mul = 1
for i in range(1, le):
    mul = (mul * i) % mod
    M.append(mul)

L0 = n//2+3
L1 = n+1

D = [[0 for i in range(L1)] for j in range(L0)]
# D[区間数][直近の区間の長さ] = 通り数
ND = [[0 for i in range(L1)] for j in range(L0)]

INVS = [0] + [inv(i) for i in range(1, n+1)]

D[1][1] = 1
for z in range(2, n+1):  # 全部のパソコン数

    l0 = z//2+3
    l1 = z+1

    for i in range(l0):
        for j in range(l1):
            ND[i][j] = 0

    for i in range(l0):
        if i >= 1:
            ND[i][1] += D[i-1][0] * (z-(i-1))
            ND[i][1] %= mod
            # print(i, 1, ND[i][1], (z-(i-1)))

    for i in range(l0):
        for j in range(1, n+1):
            ND[i][0] += D[i][j]
            ND[i][0] %= mod

    for i in range(l0):
        for j in range(l1):
            if j >= 2:
                p = D[i][j-1]
                p *= (z-(i-1))
                p %= mod
                p *= INVS[j] * 2
                p %= mod
                ND[i][j] += p
                ND[i][j] %= mod

    for i in range(l0):
        for j in range(l1):
            D[i][j] = ND[i][j]
    # D = ND[:]

    # print(z, D)

ans = 0
for i in range(L0):
    for j in range(1, L1):
        ans += D[i][j]
        ans %= mod
print(ans)
