def main(n):
    """
    根据规模 n 生成测试数据 (x, k)，并计算结果：
    若 x == 0，则结果为 0；
    否则结果为 (2^(k+1)*x - 2^k + 1) mod 1e9+7。
    """
    mod = 1000000007

    # 生成测试数据示例：
    # 让 x 随 n 变化，k 为 n 的平方（可根据需要调整生成规则）
    x = n
    k = n * n

    if x == 0:
        ans = 0
    else:
        ans = (pow(2, k + 1, mod) * x - pow(2, k, mod) + 1 + mod) % mod

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)