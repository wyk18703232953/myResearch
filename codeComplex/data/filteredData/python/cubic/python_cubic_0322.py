from random import randint

def main(n: int):
    # 1) 根据规模 n 生成 a, b, c
    #    这里简单设为与 n 同数量级，可按需调整生成策略
    a = max(1, n)
    b = max(1, n)
    c = max(1, n)

    # 2) 生成测试数据 x, y, z，元素值范围可根据需要调整
    x = [randint(1, 10**6) for _ in range(a)]
    y = [randint(1, 10**6) for _ in range(b)]
    z = [randint(1, 10**6) for _ in range(c)]

    # 保持与原程序一致：降序排序
    x.sort(reverse=True)
    y.sort(reverse=True)
    z.sort(reverse=True)

    # 3D DP，与原逻辑一致
    dp = [[[0 for _ in range(c + 2)] for _ in range(b + 2)] for _ in range(a + 1)]
    ans = 0

    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                cur = dp[i][j][k]
                if i < a and j < b:
                    val = cur + x[i] * y[j]
                    if val > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = val
                if i < a and k < c:
                    val = cur + x[i] * z[k]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val
                if j < b and k < c:
                    val = cur + y[j] * z[k]
                    if val > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = val
                if cur > ans:
                    ans = cur

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(3)，可根据需要修改 n
    main(3)