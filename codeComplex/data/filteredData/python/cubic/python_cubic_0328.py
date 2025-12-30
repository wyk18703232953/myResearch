import random

def main(n):
    # n 为总规模，这里简单地按比例拆成三个序列长度
    # 可根据需要调整拆分策略
    n0 = n // 3
    n1 = (n - n0) // 2
    n2 = n - n0 - n1
    sizes = [n0, n1, n2]

    # 生成测试数据：随机整数，范围可根据需要调整
    a = []
    for length in sizes:
        arr = [random.randint(1, 1000) for _ in range(length)]
        arr.sort(reverse=True)
        a.append(arr)

    dp = [[[0 for _ in range(sizes[2] + 1)]
           for _ in range(sizes[1] + 1)]
           for _ in range(sizes[0] + 1)]
    ans = 0

    for i in range(sizes[0] + 1):
        for j in range(sizes[1] + 1):
            for k in range(sizes[2] + 1):
                cur = dp[i][j][k]
                if i < sizes[0] and j < sizes[1]:
                    dp[i + 1][j + 1][k] = max(
                        dp[i + 1][j + 1][k],
                        cur + a[0][i] * a[1][j]
                    )
                if i < sizes[0] and k < sizes[2]:
                    dp[i + 1][j][k + 1] = max(
                        dp[i + 1][j][k + 1],
                        cur + a[0][i] * a[2][k]
                    )
                if j < sizes[1] and k < sizes[2]:
                    dp[i][j + 1][k + 1] = max(
                        dp[i][j + 1][k + 1],
                        cur + a[1][j] * a[2][k]
                    )
                if cur > ans:
                    ans = cur

    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：规模为 30
    main(30)