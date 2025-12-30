import random

def main(n: int):
    # 生成规模为 n 的测试数据
    # 原问题中每个点是 (x, r)，这里随机生成：
    # x 在 [0, 10**6]，r 在 [0, 10**6]
    points = [(random.randint(0, 10**6), random.randint(0, 10**6)) for _ in range(n)]

    # 按照原程序逻辑处理
    p = [(-(10**6), 0)] + sorted(points)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        l, r = 0, i
        while r - l > 1:
            mid = (l + r) >> 1
            if p[i][0] - p[i][1] <= p[mid][0]:
                r = mid
            else:
                l = mid
        dp[i] = i - r + dp[r - 1]

    ans = min(dp[i] + (n - i) for i in range(1, n + 1))
    print(ans)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)