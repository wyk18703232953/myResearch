def main(n):
    """
    规模 n 用于生成测试数据：
    - x = n
    - k = 2 * n
    程序计算原逻辑的结果并打印。
    """
    mod = 1000000007

    # 根据 n 生成测试数据
    x = n
    k = 2 * n

    res = pow(2, k, mod) * (2 * x - 1) + 1
    res %= mod
    if x == 0:
        res = 0

    print(res)


if __name__ == "__main__":
    # 示例：可以在此处修改测试规模 n
    main(5)