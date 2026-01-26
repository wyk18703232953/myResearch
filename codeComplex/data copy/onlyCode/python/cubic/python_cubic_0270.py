from sys import stdin

rints = lambda: [int(x) for x in stdin.readline().split()]


def dp(r1, g1, b1):
    if mem[r1][g1][b1] != -1:
        return mem[r1][g1][b1]

    v1, v2, v3 = 0, 0, 0

    if r1 < r:
        if g1 < g:
            v1 = (ar[r1] * ag[g1]) + dp(r1 + 1, g1 + 1, b1)
        if b1 < b:
            v2 = (ar[r1] * ab[b1]) + dp(r1 + 1, g1, b1 + 1)

    if g1 < g and b1 < b:
        v3 = (ag[g1] * ab[b1]) + dp(r1, g1 + 1, b1 + 1)

    mem[r1][g1][b1] = max(v1, v2, v3)

    return mem[r1][g1][b1]


r, g, b = rints()
ar, ag, ab = [sorted(rints(), reverse=True) for _ in range(3)]
mem = [[[-1 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
print(dp(0, 0, 0))
