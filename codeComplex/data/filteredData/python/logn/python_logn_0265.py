def main(n):
    """
    n 为规模参数，用来生成测试数据 (x, k)。
    这里示例性地将 x = n, k = n // 2，你可根据需要更改生成方式。
    """
    mod = 1000000007

    # 根据 n 生成测试数据
    x = n
    k = n // 2

    if k == 0:
        ans = (2 * x) % mod
    elif x == 0:
        ans = 0
    else:
        ans = ((2 * x - 1) * pow(2, k, mod) + 1) % mod

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)