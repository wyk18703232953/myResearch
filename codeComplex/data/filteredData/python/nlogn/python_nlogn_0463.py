import random

def main(n):
    # 生成测试数据
    # 约束：1 <= k <= n
    k = random.randint(1, n)
    # 生成数组 arr，元素范围可自行调整
    arr = [random.randint(1, 100) for _ in range(n)]

    # 以下为原程序逻辑
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

    length = len(dp)
    for i in range(1, length - 1):
        print(dp[i] - dp[i - 1], end=" ")
    print(n - 1 - dp[length - 2])

if __name__ == "__main__":
    # 示例：运行规模为 n=10
    main(10)