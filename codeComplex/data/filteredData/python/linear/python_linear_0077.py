import random

def main(n: int):
    # 生成测试数据：
    # a 为长度 n 的 0/1 字符串
    # b 为长度 m 的 0/1 字符串，这里设 m >= n，例如 m = 2n
    m = 2 * n
    a = ''.join(random.choice('01') for _ in range(n))
    b = ''.join(random.choice('01') for _ in range(m))

    # 原逻辑开始
    mod = 10**9 + 7  # 虽然原代码未实际用到 mod，但保留变量定义

    n = len(a)
    m = len(b)
    dp = [[0 for _ in range(2)] for _ in range(m + 1)]

    dp[1][0] = (int(b[0]) ^ 1)
    dp[1][1] = int(b[0])
    for i in range(2, m + 1):
        dp[i][0] = dp[i - 1][0] + (int(b[i - 1]) ^ 1)
        dp[i][1] = dp[i - 1][1] + int(b[i - 1])

    ans = 0
    for i in range(n):
        count0 = dp[m - n + i + 1][0] - dp[i][0]
        count1 = dp[m - n + i + 1][1] - dp[i][1]
        ans += count0 * int(a[i]) + count1 * (int(a[i]) ^ 1)

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5) 进行测试
    main(5)