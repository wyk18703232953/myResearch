from random import randint

def main(n):
    # 生成测试数据：长度为 n 的数组 a，元素取值 1..n
    a = [randint(1, n) for _ in range(n)]

    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = a[i]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            for k in range(i, j):
                if dp[i][k] and dp[i][k] == dp[k + 1][j]:
                    dp[i][j] = dp[i][k] + 1

    INF = 10 ** 10
    b = [INF] * (n + 1)
    b[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j][i - 1]:
                b[i] = min(b[i], b[j] + 1)

    print(b[n])
    return b[n]

if __name__ == "__main__":
    # 示例：可以根据需要修改 n
    main(10)