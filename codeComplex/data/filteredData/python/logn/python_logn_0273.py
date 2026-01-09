def main(n: int):
    """
    根据规模 n 生成测试数据 (x, k)，并计算：
        若 x == 0，则结果为 0
        否则结果为 ((2^(k+1) * x) - (2^k - 1)) mod (1e9+7)
    这里简单用 n 来构造 (x, k)：
        x = n
        k = n
    如需其他生成方式，可在此处调整。
    """
    mod = 10**9 + 7

    # 根据 n 生成测试数据
    x = n
    k = n

    if x == 0:
        result = 0

    else:
        result = ((pow(2, k + 1, mod) * x) - (pow(2, k, mod) - 1)) % mod

    # print(result)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    main(10)