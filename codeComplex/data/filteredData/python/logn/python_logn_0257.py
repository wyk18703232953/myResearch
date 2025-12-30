MOD = 1000000007

def main(n: int):
    """
    n 作为规模参数，用于生成测试数据 (x, k)。
    这里示例使用简单的可重复规则：
      x = n
      k = n * 2
    可根据需要自行调整生成策略。
    """
    # 生成测试数据
    x = n
    k = n * 2

    if x > 0:
        r = (pow(2, k + 1, MOD) * x - pow(2, k, MOD) + 1 + MOD * 10) % MOD
    else:
        r = 0

    print(r)


if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模
    main(10)