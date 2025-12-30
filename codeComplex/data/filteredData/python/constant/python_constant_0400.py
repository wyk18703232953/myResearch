import random

def get(a, x):
    return (a[0][x] == "0") + (a[1][x] == "0")

def main(n):
    # 3. 根据 n 生成测试数据：这里生成两行、长度为 n 的只含 '0'/'1' 的随机串
    a = [
        ''.join(random.choice('01') for _ in range(n)),
        ''.join(random.choice('01') for _ in range(n))
    ]

    if n == 1:
        print(0)
        return

    dp = [[-1, -1, -1] for _ in range(n)]
    z = get(a, 0)
    dp[0][z] = 0
    for i in range(1, n):
        z = get(a, i)
        if z == 0:
            dp[i][0] = max(dp[i - 1])
        elif z == 1:
            dp[i][0] = dp[i - 1][2] + 1
            dp[i][1] = max(dp[i - 1])
        elif z == 2:
            dp[i][0] = max(dp[i - 1][1] + 1, dp[i - 1][2] + (i != 1))
            dp[i][1] = dp[i - 1][2] + 1
            dp[i][2] = max(dp[i - 1])

    print(max(dp[-1]))


# 示例：需要时可调用 main(n)
# main(10)