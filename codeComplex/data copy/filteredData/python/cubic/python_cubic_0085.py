import os
from io import BytesIO, IOBase

def algorithm(n, k, card, fav, joy):
    dp = [[0] * (n * k + 1) for _ in range(n + 1)]
    for i in range(len(joy)):
        dp[1][i] = joy[i]
    for i in range(len(joy), n * k + 1):
        dp[1][i] = joy[-1]
    for i in range(2, n + 1):
        for j in range(1, n * k + 1):
            for kk in range(min(k + 1, j + 1)):
                dp[i][j] = max(dp[i][j], dp[i - 1][j - kk] + dp[1][kk])
    LIMIT = 10 ** 5 + 1
    tot = [0] * LIMIT
    for x in card:
        if 0 <= x < LIMIT:
            tot[x] += 1
    tot1 = [0] * LIMIT
    for x in fav:
        if 0 <= x < LIMIT:
            tot1[x] += 1
    ans = 0
    for i in range(LIMIT):
        if tot1[i] <= n and tot[i] <= n * k:
            ans += dp[tot1[i]][tot[i]]
    return ans

def generate_data(n):
    if n <= 0:
        return 0, 0, [], [], [0]
    k = max(1, n // 3)
    m = n
    card = [i % (10 ** 5) for i in range(1, m + 1)]
    fav = [(i * 2) % (10 ** 5) for i in range(1, m + 1)]
    joy_len = min(k + 1, n + 2)
    joy = [0] + [i % 7 + 1 for i in range(1, joy_len)]
    return n, k, card, fav, joy

def main(n):
    n, k, card, fav, joy = generate_data(n)
    result = algorithm(n, k, card, fav, joy)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)