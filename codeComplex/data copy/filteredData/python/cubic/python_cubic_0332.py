import bisect as bi

def yes():
    # print('YES')
    pass

def no():
    # print('NO')
    pass

def dict(a):
    d = {}
    for x in a:
        if d.get(x, -1) != -1:
            d[x] += 1

        else:
            d[x] = 1
    return d

def find_gt(a, x):
    i = bi.bisect_left(a, x)
    if i != len(a):
        return i

    else:
        return -1

def cal(r, g, b, dp, R, G, B, nr, ng, nb):
    if dp[r][g][b] != -1:
        return dp[r][g][b]
    best = 0
    if r < nr and g < ng:
        best = max(best, cal(r + 1, g + 1, b, dp, R, G, B, nr, ng, nb) + R[r] * G[g])
    if r < nr and b < nb:
        best = max(best, cal(r + 1, g, b + 1, dp, R, G, B, nr, ng, nb) + R[r] * B[b])
    if g < ng and b < nb:
        best = max(best, cal(r, g + 1, b + 1, dp, R, G, B, nr, ng, nb) + B[b] * G[g])
    dp[r][g][b] = best
    return dp[r][g][b]

def generate_data(n):
    # Map n to sizes of R, G, B; keep small to avoid huge 3D DP
    nr = max(1, n // 3)
    ng = max(1, n // 3)
    nb = max(1, n - nr - ng)
    max_len = 200
    nr = min(nr, max_len)
    ng = min(ng, max_len)
    nb = min(nb, max_len)

    R = [i + 1 for i in range(nr)]
    G = [2 * (i + 1) for i in range(ng)]
    B = [3 * (i + 1) for i in range(nb)]
    return nr, ng, nb, R, G, B

def main(n):
    nr, ng, nb, R, G, B = generate_data(n)
    max_dim = 200
    dp = [[[-1 for _ in range(max_dim + 1)] for _ in range(max_dim + 1)] for _ in range(max_dim + 1)]
    R.sort(reverse=True)
    G.sort(reverse=True)
    B.sort(reverse=True)
    result = cal(0, 0, 0, dp, R, G, B, nr, ng, nb)
    # print(result)
    pass

M = 998244353
P = 1000000007

if __name__ == "__main__":
    main(10)