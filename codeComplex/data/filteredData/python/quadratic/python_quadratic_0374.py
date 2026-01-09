MOD = 998244353


def norm(x):
    return (x % MOD + MOD) % MOD


def main(n, k=None):
    # 若未提供 k，则用一个与规模 n 相关的测试值
    if k is None:
        k = n * n // 2  # 可按需要修改测试数据规则

    dp1 = [0]
    dp2 = [0]

    for i in range(n):
        l = [1]
        cur = 0
        for j in range(n + 1):
            cur += l[j]
            if j > i:
                cur -= l[j - i - 1]
            cur = norm(cur)
            l.append(cur)
        dp1.append(l[n])
        dp2.append(norm(dp1[i + 1] - dp1[i]))

    ans = 0
    for i in range(n + 1):
        for j in range(n + 1):
            if i * j < k:
                ans = norm(ans + dp2[i] * dp2[j])

    ans = norm(ans * 2)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：自动生成规模为 5 的测试数据
    main(5)