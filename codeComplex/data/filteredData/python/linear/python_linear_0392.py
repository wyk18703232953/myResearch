def main(n):
    mod = 998244353
    powe = [1]
    for _ in range(10**6):
        powe.append((powe[-1] * 2) % mod)

    if n <= 0:
        # print(0)
        pass
        return

    # 确定性生成长度为 n 的数组 a
    # 模拟原题中一般的整数范围
    a = [(i * 37 + 13) % mod for i in range(n)]

    ans = (a[0] * powe[n - 1]) % mod
    dp = a[0]
    dp1 = 0

    for i in range(1, n):
        if i == 1:
            dp = (dp + a[i]) % mod

        else:
            dp = (dp * 2 + a[i] - dp1) % mod
        ans = (ans + powe[n - i - 1] * dp) % mod
        dp1 = a[i]

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：输入规模为 10
    main(10)