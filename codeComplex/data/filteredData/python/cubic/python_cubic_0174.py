import random

def main(n: int):
    # 1. 生成测试数据：长度为 n 的整数数组 a
    # 这里示例为 1~3 之间的随机整数，可按需要修改
    a = [random.randint(1, 3) for _ in range(n)]

    rows, cols = (n + 1, n + 1)
    dp = [[-1 for _ in range(rows)] for _ in range(cols)]

    # 初始化对角线
    for i in range(n):
        dp[i][i] = a[i]

    # 区间 DP
    for last in range(1, n):
        for first in range(last - 1, -1, -1):
            for mid in range(last, first, -1):
                if (
                    dp[first][mid - 1] != -1
                    and dp[mid][last] != -1
                    and dp[first][mid - 1] == dp[mid][last]
                ):
                    dp[first][last] = dp[first][mid - 1] + 1

    ans = [0 for _ in range(n)]
    for i in range(n):
        ans[i] = i + 1

    for i in range(n):
        for j in range(i, -1, -1):
            if j - 1 >= 0:
                if dp[j][i] != -1:
                    ans[i] = min(ans[i], ans[j - 1] + 1)
            elif dp[0][i] != -1:
                ans[i] = 1

    # 原程序只输出 ans[n-1]
    print(ans[n - 1])


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改规模
    main(5)