from collections import deque

PI = float('inf')
M = 10**9 + 7

def main(n):
    # 生成确定性的输入数据：
    # 原程序读入一个整数 n，然后读入 n 行字符串 s[i]，每行要么是 'f' 要么是其他（代表 's'）
    # 这里用 n 来表示行数，并以简单规律生成 'f'/'s' 序列
    # 例如：索引为偶数的位置为 'f'，奇数为 's'
    if n <= 0:
        print(0)
        return

    s = ['f' if i % 2 == 0 else 's' for i in range(n)]

    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n):
        for j in range(n):
            if i >= 1 and s[i - 1] == 'f':
                if j >= 1:
                    dp[i][j] = dp[i - 1][j - 1] - dp[i - 1][j]
            elif i >= 1:
                dp[i][j] = dp[i - 1][j]
            dp[i][j] %= M
        for k in range(n - 1, -1, -1):
            dp[i][k] = (dp[i][k] + dp[i][k + 1]) % M

    print(dp[n - 1][0] % M)


if __name__ == "__main__":
    # 示例：用规模 n=5 运行
    main(5)