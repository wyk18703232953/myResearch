def main(n: int):
    """
    n 为规模参数，这里用来生成测试数据：
    - X = n
    - K = n 的平方
    可根据需要修改生成规则。
    """
    mod = 1000000007

    # 根据 n 生成测试数据（示例规则）
    X = n
    K = n * n

    res = X * pow(2, K + 1, mod) - pow(2, K, mod) + 1
    while res < 0:
        res += mod

    if X == 0:
        print(0)
    else:
        print(res % mod)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)