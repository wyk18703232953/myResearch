def main(n: int):
    """
    按规模 n 生成一组 (x, k) 测试数据并计算结果。
    这里示例策略：
    - x = n
    - k = n
    可根据需要调整生成规则。
    """
    mod = 10**9 + 7

    # 根据 n 生成测试数据
    x = n
    k = n

    if x == 0:
        # print(0)
        pass

    else:
        val1 = pow(2, k + 1, mod) * x
        val2 = pow(2, k, mod) - 1
        val1 -= val2
        val1 %= mod
        # print(val1)
        pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)