MOD = 998244353

def norm(x):
    return (x % MOD + MOD) % MOD

def main(n):
    # 生成测试数据：给定规模 n，自行构造一个 k
    # 这里选取 k = n^2 // 2，保证有一定数量的 (i, j) 对被计入
    k = (n * n) // 2

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
    # 示例：调用 main(5)
    main(5)