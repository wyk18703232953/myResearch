def main(n):
    """
    n 作为规模参数，用于生成测试数据：
    这里简单设定：
        x = n
        k = n // 2
    可按需要自行调整生成策略。
    """
    MOD = 1000000007

    # 生成测试数据
    x = n
    k = n // 2

    if x == 0:
        print(0)
    else:
        nn = pow(2, k, MOD)
        result = (nn * 2 * x - nn + 1) % MOD
        print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)