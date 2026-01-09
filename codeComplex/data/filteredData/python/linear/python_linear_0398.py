def main(n):
    MOD = 998244353
    # 生成确定性输入数组 a，长度为 n
    # 元素构造：a[i] = (i * 3 + 1) % MOD
    a = [(i * 3 + 1) % MOD for i in range(n)]
    if n == 0:
        # print(0)
        pass
        return
    s = a[0] % MOD
    y = a[0]
    for x in a[1:]:
        s = s * 2 + y + x
        y = y * 2 + x
        s %= MOD
        y %= MOD
    # print(s)
    pass
if __name__ == "__main__":
    main(10)