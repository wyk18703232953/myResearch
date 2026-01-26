def main(n: int):
    """
    n: 规模，用于生成测试数据 (x, k)。
    这里示例数据生成方式为：
        x = n
        k = n
    可根据需要修改生成逻辑。
    """
    mod = 1000000007

    # 根据 n 生成测试数据 (x, k)
    x = n
    k = n

    if x == 0:
        # print(0)
        pass

    else:
        ans = (pow(2, k + 1, mod) * x - pow(2, k, mod) + 1) % mod
        # print(int(ans))
        pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)