def main(n):
    mod = 998244353

    # 生成测试数据：这里示例为 a[i] = i+1
    # 可按需要改为其他生成方式
    a = [(i + 1) % mod for i in range(n)]

    ans = 0
    # 1/2 在模 mod 下的逆元
    inv2 = pow(2, mod - 2, mod)
    p = inv2  # p = 1/2

    for i in range(n):
        ans = (ans + (i + 2) * (p * a[n - i - 1] % mod) % mod) % mod
        p = (2 * p) % mod

    print(ans % mod)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)