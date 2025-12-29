from sys import setrecursionlimit
import random

setrecursionlimit(100000)


def dfs(r, g, b, rr, gg, bb, dp):
    if r < 0 or g < 0 or b < 0:
        return 0

    if dp[r][g][b] != -1:
        return dp[r][g][b]

    x = y = z = 0

    if r != 0 and g != 0:
        x = rr[r - 1] * gg[g - 1] + dfs(r - 1, g - 1, b, rr, gg, bb, dp)
    if r != 0 and b != 0:
        y = rr[r - 1] * bb[b - 1] + dfs(r - 1, g, b - 1, rr, gg, bb, dp)
    if b != 0 and g != 0:
        z = bb[b - 1] * gg[g - 1] + dfs(r, g - 1, b - 1, rr, gg, bb, dp)

    dp[r][g][b] = max(x, y, z)
    return dp[r][g][b]


def main(n: int):
    # 根据规模 n 生成测试数据：
    # 将 r, g, b 设为不超过 n 的正整数
    # 并生成对应长度的正整数数组
    if n <= 0:
        return 0

    # 这里简单选择 r, g, b 不超过 n，且总规模与 n 同量级
    r = random.randint(1, n)
    g = random.randint(1, n)
    b = random.randint(1, n)

    # 生成随机正整数，范围可按需调整
    rr = [random.randint(1, 10**4) for _ in range(r)]
    gg = [random.randint(1, 10**4) for _ in range(g)]
    bb = [random.randint(1, 10**4) for _ in range(b)]

    rr.sort()
    gg.sort()
    bb.sort()

    dp = [[[-1] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]
    ans = dfs(r, g, b, rr, gg, bb, dp)
    print(ans)
    return ans


if __name__ == "__main__":
    # 示例：使用 n = 5 运行一次
    main(5)