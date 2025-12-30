import random


def main(n: int):
    # 生成测试数据
    # a: 严格递增序列，更容易出现合法三元组
    a = sorted(random.sample(range(1, 10 * n + 1), n))
    # b: 随机权重
    b = [random.randint(1, 100) for _ in range(n)]

    PI = float('inf')
    ans = PI
    dp = [[PI for _ in range(4)] for _ in range(n)]

    for i in range(n):
        dp[i][1] = b[i]
        for j in range(i):
            if a[j] < a[i]:
                dp[i][2] = min(dp[i][2], dp[j][1] + b[i])
                dp[i][3] = min(dp[i][3], dp[j][2] + b[i])
                ans = min(ans, dp[i][3])

    print("n:", n)
    print("a:", a)
    print("b:", b)
    print("answer:", ans if ans != PI else -1)


if __name__ == "__main__":
    # 可根据需要修改规模
    main(10)