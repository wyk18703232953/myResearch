import random

MOD = 1000000007

def main(n: int) -> int:
    """
    n: problem size, also the length of generated command sequence.
    Returns the final dp[0] result.
    """
    # 根据 n 生成测试数据：长度为 n 的随机指令序列，仅包含 'f' 和 's'
    # 为了可重复性，可按需要固定随机种子；这里不固定种子
    commands = [random.choice(("f", "s")) for _ in range(n)]

    dp = [1]
    for c in commands:
        if c == "f":
            dp.insert(0, 0)
        else:
            for i in range(len(dp) - 2, -1, -1):
                dp[i] = (dp[i] + dp[i + 1]) % MOD
    return dp[0]


if __name__ == "__main__":
    # 示例：运行 main(5) 并打印结果
    print(main(5))