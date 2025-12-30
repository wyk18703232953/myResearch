import random

MOD = 10 ** 9 + 7


def main(n: int) -> int:
    """
    生成规模为 n 的测试数据（长度为 n 的字符串序列，每个为 'f' 或 's'），
    然后按照原程序逻辑计算结果并返回。
    """
    # 生成测试数据：长度为 n 的字符串列表，每个为 'f' 或 's'
    # 你可以根据需要调整分布，这里简单用均匀随机
    seq = ['f' if random.randint(0, 1) == 0 else 's' for _ in range(n)]

    # 原程序逻辑开始
    dp = [[0 for _ in range(n + 5)] for _ in range(n + 5)]
    prev = "-1"

    for i in range(n):
        p = seq[i]
        if i == 0:
            dp[i][0] = 1
        else:
            c = 0
            if prev == 'f':
                for j in range(n):
                    dp[i][j + 1] = dp[i - 1][j]
            else:
                for j in range(n, -1, -1):
                    c = (c + dp[i - 1][j]) % MOD
                    dp[i][j] = c
        prev = p

    return sum(dp[n - 1]) % MOD


if __name__ == "__main__":
    # 示例调用：可以修改这里的 n 来本地测试
    n = 5
    print(main(n))