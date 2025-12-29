from math import gcd, ceil
import random


def prod(a, mod=10 ** 9 + 7):
    ans = 1
    for each in a:
        ans = (ans * each) % mod
    return ans


def lcm(a, b):
    return a * b // gcd(a, b)


def binary(x, length=16):
    y = bin(x)[2:]
    return y if len(y) >= length else "0" * (length - len(y)) + y


def main(n: int):
    # 生成测试数据：长度为 n 的数组 a，元素在 [1, 5] 内
    #（可按需要调整范围）
    random.seed(0)
    a = [random.randint(1, 5) for _ in range(n)]

    dp = [[False] * (n + 2) for _ in range(n + 2)]
    # dp[i][j] -> 如果 a[i..j] 能被规约成一个元素，则为该元素的值；否则为 False
    dp2 = [[600] * (n + 2) for _ in range(n + 2)]

    for i in range(n):
        dp[i][i] = a[i]
        dp2[i][i] = 1

    for diff in range(1, n):
        for i in range(n - diff):
            # 区间 [i, i+diff]
            r = i + diff
            for j in range(i, r):
                if dp[i][j] == dp[j + 1][r] and dp[i][j]:
                    dp[i][r] = dp[i][j] + 1
                    dp2[i][r] = 1
                dp2[i][r] = min(dp2[i][r], dp2[i][j] + dp2[j + 1][r])
            if not dp2[i][r]:
                dp2[i][r] = min(dp2[i + 1][r] + 1, dp2[i][r - 1] + 1)

    print(dp2[0][n - 1])


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)