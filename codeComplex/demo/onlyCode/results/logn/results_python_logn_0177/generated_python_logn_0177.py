MOD = 1000000009

def main(n: int):
    """
    n: 规模参数，用于生成测试数据 (n, m, k)
    测试数据构造规则（可按需要调整）：
      m = 2 * n
      k = max(1, n // 2)
    """
    # 依据规模 n 构造测试数据
    m = 2 * n
    k = max(1, n // 2)

    # 原逻辑开始
    x = m - (n // k * (k - 1) + (n % k))

    if x <= 0:
        print(m % MOD)
        return

    result = ((m - x) + ((pow(2, x + 1, MOD) + 2 * MOD) - 2) * k - x * (k - 1)) % MOD
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)