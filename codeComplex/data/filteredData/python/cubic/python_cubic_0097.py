MOD = 998244353

def norm(x):
    return (x % MOD + MOD) % MOD

def main(n):
    # 生成测试数据：n 给定，构造一个与 n 同量级的 k
    # 这里示例设 k = n * n // 2，可根据需要调整
    k = n * n // 2

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
    # 示范调用，规模可自行调整
    main(5)