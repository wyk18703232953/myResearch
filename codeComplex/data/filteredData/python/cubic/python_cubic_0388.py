from array import array
import random

def main(n: int):
    # 生成测试数据：给定规模 n，构造一个模数 M
    # 可以根据需要调整 M 的生成方式，这里取一个较大的质数附近值
    M = 10**9 + 7

    # 组合数 C(i, j) mod M，0 <= i, j <= n
    comb = [[0] * (n + 1) for _ in range(n + 1)]
    comb[0][0] = 1
    for i in range(1, n + 1):
        comb[i][0] = 1
        comb[i][i] = 1
        for j in range(1, i):
            comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % M

    dp = [array('i', [0] * (n + 1)) for _ in range(n + 1)]
    # number of partitions ; number of computer
    for i in range(1, n + 1):
        dp[i][0] = pow(2, i - 1, M)

    for j in range(1, n + 1):
        for i in range(3, n + 1):
            val = dp[i][j]
            for x in range(1, i - 1):
                val = (val +
                       dp[i - 1 - x][j - 1] *
                       dp[x][0] *
                       comb[i - j][x]) % M
            dp[i][j] = val

    su = 0
    for i in range(n + 1):
        su = (su + dp[n][i]) % M

    print(su)


if __name__ == "__main__":
    # 示例：可以在这里调用 main，并根据需要选择 n
    test_n = 10  # 可修改为任意规模
    main(test_n)