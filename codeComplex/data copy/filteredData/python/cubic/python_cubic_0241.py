from sys import setrecursionlimit

setrecursionlimit(100000)


def dfs(r, g, b, rr, gg, bb, dp):
    if r < 0 or g < 0 or b < 0:
        return 0
    if dp[r][g][b] != -1:
        return dp[r][g][b]

    x = 0
    y = 0
    z = 0

    if r != 0 and g != 0:
        x = rr[r - 1] * gg[g - 1] + dfs(r - 1, g - 1, b, rr, gg, bb, dp)
    if r != 0 and b != 0:
        y = rr[r - 1] * bb[b - 1] + dfs(r - 1, g, b - 1, rr, gg, bb, dp)
    if b != 0 and g != 0:
        z = bb[b - 1] * gg[g - 1] + dfs(r, g - 1, b - 1, rr, gg, bb, dp)

    dp[r][g][b] = max(x, y, z)
    return dp[r][g][b]


def main(n):
    # n 控制三个数组的规模，这里令 r = g = b = n
    r = n
    g = n
    b = n

    # 确定性生成 rr, gg, bb
    rr = [i for i in range(1, r + 1)]
    gg = [i * 2 for i in range(1, g + 1)]
    bb = [i * 3 for i in range(1, b + 1)]

    rr.sort()
    gg.sort()
    bb.sort()

    dp = [[[-1] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    ans = dfs(r, g, b, rr, gg, bb, dp)
    # print(ans)
    pass
if __name__ == "__main__":
    main(5)