def main(n):
    # 映射：n -> x, k
    # 保证规模随 n 增长，同时保持确定性
    x = n * n + 3 * n + 7
    k = max(0, n - 1)

    if x == 0:
        # print(0)
        pass
        return

    mod = 10 ** 9 + 7

    a = ((x % mod) * pow(2, k + 1, mod)) % mod

    # print((a - (pow(2, k, mod) - 1)) % mod)
    pass
if __name__ == "__main__":
    main(10)