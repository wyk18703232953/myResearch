def main(n):
    # 生成测试数据：根据规模 n 构造一个模数 mod
    # 可按需修改生成规则
    mod = 10**9 + 7

    MAXN = 500  # 与原程序一致的上界

    def getc():
        # 预处理组合数 C(i, j) mod mod，范围与原代码保持一致
        f = [[0] * MAXN for _ in range(MAXN)]
        for i in range(MAXN):
            f[i][0] = 1
        f[1][0] = 1
        f[1][1] = 1
        for i in range(2, 411):
            for j in range(1, i + 1):
                f[i][j] = (f[i - 1][j - 1] + f[i - 1][j]) % mod
        return f

    # 防止 n 超出预设数组范围
    if n >= MAXN:
        raise ValueError(f"n 必须小于 {MAXN}，当前为 {n}")

    f = [[0] * MAXN for _ in range(MAXN)]
    c = getc()

    mi_2 = [0] * MAXN
    mi_2[0] = 1
    for i in range(1, MAXN):
        mi_2[i] = mi_2[i - 1] * 2 % mod

    for i in range(1, n + 1):
        for j in range(0, i // 2 + 1):
            if j == 0:
                f[i][j] = mi_2[i - 1]

            else:
                val = 0
                for k in range(2, i):
                    val = (val +
                           (mi_2[k - 2] * f[i - k][j - 1] % mod) *
                           c[i - j][k - 1] % mod) % mod
                f[i][j] = val

    ans = 0
    for i in range(0, n + 1):
        ans = (ans + f[n][i]) % mod

    # print(ans)
    pass


# 示例调用（可根据需要注释或修改）
if __name__ == "__main__":
    main(10)