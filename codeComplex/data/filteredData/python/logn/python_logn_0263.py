MOD = 10 ** 9 + 7


def bin_pow(n, k):
    res = 1
    while k:
        if k & 1:
            res = (res * n) % MOD
        n = (n * n) % MOD
        k >>= 1
    return res


def main(n):
    """
    n 为规模参数：
    这里用 n 来生成测试数据：
      x = n
      k = n
    原逻辑为：
      输入 x, k
      若 x == 0 输出 0
      否则输出 (2^(k+1) * x - 2^k + 1) mod MOD
    """
    x = n
    k = n

    if x == 0:
        ans = 0
    else:
        ans = (bin_pow(2, k + 1) * x - bin_pow(2, k) + 1) % MOD

    print(ans)


if __name__ == "__main__":
    # 示例：使用 n=10 运行
    main(10)