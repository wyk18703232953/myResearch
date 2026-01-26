def main(n):
    mod = 10**9 + 7

    # 根据规模 n 生成测试数据 (x, k)
    # 示例：x = n, k = n // 2
    x = n
    k = n // 2

    if x == 0:
        # print(0)
        pass
        return

    p = pow(2, k, mod)
    res = (((2 * x) % mod + mod - 1) % mod)
    res = ((res * p) % mod + 1) % mod
    # print(res)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)