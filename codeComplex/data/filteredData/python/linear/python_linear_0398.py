def main(n):
    # n 作为数组长度
    if n <= 0:
        print(0)
        return

    MOD = 998244353
    # 确定性生成长度为 n 的整数数组
    a = [(i * 3 + 1) % MOD for i in range(n)]

    s = a[0] % MOD
    y = a[0]
    for x in a[1:]:
        s = s * 2 + y + x
        y = y * 2 + x
        s %= MOD
        y %= MOD

    print(s)


if __name__ == "__main__":
    # 示例：使用规模 n=5 运行
    main(5)