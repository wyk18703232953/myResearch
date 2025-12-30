def main(n):
    """
    n 为规模参数，这里用来生成测试数据：
    例如令 x = n, k = n。
    可以根据需要修改生成方式。
    """
    x = n
    k = n

    if x == 0:
        print(0)
        return

    mod = 10**9 + 7
    p = pow(2, k, mod)
    print((2 * p * x - p + 1) % mod)


if __name__ == "__main__":
    # 示例：用 n = 10 作为规模调用
    main(10)