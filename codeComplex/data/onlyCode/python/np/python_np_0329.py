from sys import stdin

add = lambda a, b: (a % mod + b % mod) % mod
mod, bits = 998244353, ['00', '01', '10', '11']
pat = [[0, 1, 1, 1], [0, 0, 2, 0], [0, 2, 0, 0], [1, 1, 1, 0]]

n, k = map(int, stdin.readline().split())
mem = [[[0 for _ in range(4)] for _ in range(k + 1)] for _ in range(2)]

for i in range(4):
    val = min(bits[i].count('0'), 1) + min(bits[i].count('1'), 1)
    if val <= k:
        mem[0][val][i] = 1

for i in range(1, n):
    for j in range(1, k + 1):
        for k1 in range(4):
            for k2 in range(4):
                val = j + pat[k1][k2]
                if val <= k:
                    mem[i & 1][val][k2] = add(mem[(i - 1) & 1][j][k1], mem[i & 1][val][k2])

    for j in range(1, k + 1):
        for k1 in range(4):
            mem[(i - 1) & 1][j][k1] = 0

print(sum(mem[(n - 1) & 1][k]) % mod)
