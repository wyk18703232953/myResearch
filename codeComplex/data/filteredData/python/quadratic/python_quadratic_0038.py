from collections import deque
from random import choice, seed

PI = float('inf')
M = 10 ** 9 + 7


def main(n: int) -> int:
    """
    n: problem size (length of sequence s)
    returns: result originally printed by the program
    """
    # 固定随机种子以便复现实验，如不需要可移除或改为参数
    seed(0)

    # 根据 n 生成测试数据：s 为长度 n 的字符串列表，由 'f' 和 's' 组成
    # 原代码中是读取 n 行字符串；这里简化为随机的 'f' 或 's'
    s = [choice(['f', 's']) for _ in range(n)]

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

    return dp[n - 1][0] % M


if __name__ == "__main__":
    # 示例调用，可按需修改或删除
    print(main(5))