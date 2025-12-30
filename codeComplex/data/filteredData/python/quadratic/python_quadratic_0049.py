import random

MOD = 1000000007

def main(n: int) -> int:
    # 生成长度为 n 的测试数据，由 'f' 和 's' 组成
    # 可根据需要更换生成规则，这里简单随机生成
    cmds = [random.choice(("f", "s")) for _ in range(n)]

    dp = [1]
    for c in cmds:
        if c == "f":
            dp.insert(0, 0)
        else:
            for i in range(len(dp) - 2, -1, -1):
                dp[i] = (dp[i] + dp[i + 1]) % MOD
    return dp[0]


if __name__ == "__main__":
    # 示例：n = 5
    print(main(5))