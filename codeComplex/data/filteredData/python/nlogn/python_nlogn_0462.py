import random

def main(n, k=None, seed=0):
    # 1. 生成测试数据
    random.seed(seed)
    if k is None:
        k = max(1, n // 3)  # 默认令 k 为 n 的约三分之一，至少为 1
    k = min(k, n)          # 保证 k 不超过 n

    # 生成 n 个随机整数作为 arr
    # 数值范围可按需要调整
    arr = [random.randint(-10**9, 10**9) for _ in range(n)]

    # 2. 原逻辑开始
    l = []
    for i in range(n):
        l.append((arr[i], i))

    l.sort(reverse=True)

    dp = []
    x = 0
    for i in range(k):
        dp.append(l[i][1])
        x = x + l[i][0]

    print(x)
    dp.sort()
    dp = [-1] + dp

    ln = len(dp)
    for i in range(1, ln - 1):
        print(dp[i] - dp[i - 1], end=" ")
    print(n - 1 - dp[ln - 2])

if __name__ == "__main__":
    # 示例运行：n = 10
    main(10)