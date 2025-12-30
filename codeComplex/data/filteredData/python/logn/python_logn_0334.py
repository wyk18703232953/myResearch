def binpow(x, k, mod):
    res = 1
    while k > 0:
        if k & 1:
            res = (res * x) % mod
        x = (x * x) % mod
        k >>= 1
    return res


def main(n):
    # 根据规模 n 生成测试数据
    # 示例策略：x = n, k = n^2
    x = n
    k = n * n

    if x == 0:
        print(0)
        return

    mod = int(1e9 + 7)
    k2 = binpow(2, k, mod)
    res = (k2 * (2 * x - 1) + 1) % mod
    res %= mod

    print(int(res))


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值
    main(10)