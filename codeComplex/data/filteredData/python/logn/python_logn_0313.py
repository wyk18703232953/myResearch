def main(n):
    """
    n: 规模参数，用于生成测试数据
    这里将根据 n 生成 x, k，并执行原逻辑。
    生成规则示例：
      x = n
      k = n // 2
    可根据实际需要调整生成规则。
    """
    # 生成测试数据
    x = n
    k = n // 2

    if x == 0:
        # print(0)
        pass
        return

    m = 10**9 + 7
    p = pow(2, k + 1, m)
    q = pow(2, k, m)
    a = (x * p - q + 1) % m
    # print(a)
    pass
if __name__ == "__main__":
    # 示例运行：可以修改这里的 n 进行测试
    main(10)