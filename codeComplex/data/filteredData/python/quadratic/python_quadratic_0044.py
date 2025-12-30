import random

MOD = 1000000007

def main(n: int) -> int:
    # 生成规模为 n 的测试数据：随机由 'f' 和 's' 组成的指令序列
    # 你也可以根据需要手动改成固定模式，例如全 'f' 或全 's'
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
    # 示例调用：可以修改这里的 n 来运行不同规模的测试
    print(main(5))