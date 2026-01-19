import math

def solve(n, p):
    y = 1 << n
    dp = [[0.0] * y for _ in range(n)]
    dp[0][y - 1] = 1.0
    for i in range(y - 2, -1, -1):
        mask = 1
        for j in range(n):
            if not mask & i:
                mask <<= 1
                continue
            mask1 = 1
            for k in range(n):
                if i & mask1:
                    mask1 <<= 1
                    continue
                dp[j][i] = max(
                    dp[j][i],
                    dp[j][i | mask1] * p[j][k] + dp[k][i | mask1] * p[k][j]
                )
                mask1 <<= 1
            mask <<= 1
    return max(dp[i][1 << i] for i in range(n))

def generate_matrix(n):
    p = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                p[i][j] = 0.0
            elif i < j:
                val = ((i + 1) * (j + 2)) % 100
                prob = val / 100.0
                p[i][j] = prob
                p[j][i] = 1.0 - prob
    return p

def main(n):
    if n <= 0:
        return 0.0
    # n is the number of players; complexity grows as 2^n
    p = generate_matrix(n)
    result = solve(n, p)
    print(result)
    return result

if __name__ == "__main__":
    # example call for timing/experiments; adjust n as needed
    main(10)