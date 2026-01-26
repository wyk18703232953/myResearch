MOD = 1000000007

def main(n: int):
    """
    n 为规模参数，这里用于生成测试数据 (x, k)。
    示例：x = n, k = n
    可以根据需要调整生成规则。
    """
    x = n
    k = n

    if x == 0:
        # print(0)
        pass

    else:
        # print((pow(2, k, MOD) * (2 * x - 1) + 1) % MOD)
        pass
if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    main(10)