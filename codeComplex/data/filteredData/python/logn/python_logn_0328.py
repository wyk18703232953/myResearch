def main(n):
    """
    n 用来生成测试数据 (x, k)：
    示例策略：
    x = n
    k = n // 2
    """
    mod = 10**9 + 7
    x = n
    k = n // 2

    if x == 0:
        print(0)
    elif k == 0:
        print((2 * x) % mod)
    else:
        ans = (((pow(2, k, mod) * x - pow(2, k - 1, mod)) % mod) * 2 + 3 * mod + 1) % mod
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)