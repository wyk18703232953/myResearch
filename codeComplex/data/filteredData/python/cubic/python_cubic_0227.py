import random

def main(n):
    # 这里将原来的 n, m, v 都设为与规模 n 相关
    # 你可以按需修改，比如 m = n // 2, v = n // 3 等
    m = n
    v = n

    # 生成测试数据：a, b, c 为长度 n 的随机整数数组
    # 原代码中会把读入的值加 1（对 n,m,v），但数组本身不 +1
    # 数值范围可按需调整
    a = [random.randint(1, 1000) for _ in range(n)]
    b = [random.randint(1, 1000) for _ in range(n)]
    c = [random.randint(1, 1000) for _ in range(n)]

    # 对应原代码的 n+1, m+1, v+1（在读入时已经 +1）
    n1, m1, v1 = n + 1, m + 1, v + 1

    # 初始化 3 维 DP 数组
    dp = [[[0] * v1 for _ in range(m1)] for __ in range(n1)]

    # 排序并倒序
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    # 前面加一个 0，占位，使下标从 1 开始使用
    a = [0] + a
    b = [0] + b
    c = [0] + c

    ans = 0
    for i in range(n1):
        for j in range(m1):
            for k in range(v1):
                if i == j == k == 0:
                    continue
                if i == j == 0 or i == k == 0 or j == k == 0:
                    continue
                if i == 0:
                    dp[i][j][k] = dp[i][j - 1][k - 1] + b[j] * c[k]
                elif j == 0:
                    dp[i][j][k] = dp[i - 1][j][k - 1] + a[i] * c[k]
                elif k == 0:
                    dp[i][j][k] = dp[i - 1][j - 1][k] + a[i] * b[j]
                else:
                    dp[i][j][k] = max(
                        dp[i - 1][j - 1][k] + a[i] * b[j],
                        dp[i - 1][j][k - 1] + a[i] * c[k],
                        dp[i][j - 1][k - 1] + b[j] * c[k]
                    )
                ans = max(ans, dp[i][j][k])

    print(ans)


if __name__ == "__main__":
    # 示例调用，可以修改 n
    main(5)