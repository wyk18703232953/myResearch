import random

mod = 10**9 + 7

def main(n: int) -> int:
    # 生成测试数据：长度为 n 的字符串序列，每个元素为 'f' 或 's'
    # 保持与原程序含义一致：循环 n 次，每次读取一个字符串
    seq = ['f' if random.randint(0, 1) == 0 else 's' for _ in range(n)]

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(n):
        nx = [0] * (n + 1)
        s = seq[i]
        if s == 'f':
            nx[0] = 0
            for j in range(1, n + 1):
                nx[j] = dp[j - 1] % mod
        else:
            nx[n] = dp[n] % mod
            for j in reversed(range(n)):
                nx[j] = (nx[j + 1] + dp[j]) % mod
        if i != n - 1:
            dp = nx

    return sum(dp) % mod