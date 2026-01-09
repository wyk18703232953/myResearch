import sys

from heapq import heapify, heappush as hp, heappop as hpop


def solve_with_params(n, m, k, l1, l2):
    inf = 10 ** 18

    def check(x, y):
        return 0 <= x <= n - 1 and 0 <= y <= m - 1

    dp = [[[inf] * 21 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if check(i, j + 1):
                dp[i][j][1] = min(l1[i][j], dp[i][j][1])
            if check(i, j - 1):
                dp[i][j][1] = min(l1[i][j - 1], dp[i][j][1])
            if check(i + 1, j):
                dp[i][j][1] = min(l2[i][j], dp[i][j][1])
            if check(i - 1, j):
                dp[i][j][1] = min(l2[i - 1][j], dp[i][j][1])

    for x in range(2, k // 2 + 1):
        for i in range(n):
            for j in range(m):
                if check(i, j + 1):
                    dp[i][j][x] = min(l1[i][j] + dp[i][j + 1][x - 1], dp[i][j][x])
                if check(i, j - 1):
                    dp[i][j][x] = min(l1[i][j - 1] + dp[i][j - 1][x - 1], dp[i][j][x])
                if check(i + 1, j):
                    dp[i][j][x] = min(l2[i][j] + dp[i + 1][j][x - 1], dp[i][j][x])
                if check(i - 1, j):
                    dp[i][j][x] = min(l2[i - 1][j] + dp[i - 1][j][x - 1], dp[i][j][x])

    ans = [[-1] * m for _ in range(n)]
    if not k % 2:
        for i in range(n):
            for j in range(m):
                ans[i][j] = 2 * dp[i][j][k // 2]
    return ans


def generate_data(n):
    if n < 1:
        n = 1
    m = n
    k = 2 * min(10, n)
    l1 = [[(i * m + j) % 7 + 1 for j in range(m)] for i in range(n)]
    l2 = [[(i * m + j) % 9 + 1 for j in range(m)] for i in range(n - 1)]
    return n, m, k, l1, l2


def main(n):
    n_, m_, k_, l1, l2 = generate_data(n)
    ans = solve_with_params(n_, m_, k_, l1, l2)
    out_lines = []
    for row in ans:
        out_lines.append(" ".join(str(x) for x in row))
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main(5)