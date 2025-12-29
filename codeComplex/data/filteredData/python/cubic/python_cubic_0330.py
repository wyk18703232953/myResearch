from collections import defaultdict
import random

def main(n: int):
    # 依据规模 n 生成 R, G, B
    # 这里简单设为相同规模，也可以按需修改比例
    R = G = B = n

    # 生成测试数据：随机正整数（包含负数也可，根据原题需求调整）
    # 保证有一定范围，避免数字过大导致乘积过大
    MAX_VAL = 10**4
    red = [random.randint(1, MAX_VAL) for _ in range(R)]
    green = [random.randint(1, MAX_VAL) for _ in range(G)]
    blue = [random.randint(1, MAX_VAL) for _ in range(B)]

    red.sort(reverse=True)
    green.sort(reverse=True)
    blue.sort(reverse=True)

    # 注意：原代码有明显的索引越界和负索引问题，这里按其原始写法仅做结构迁移，
    # 若要真正可运行，需要修正 DP 转移（例如判断 i>0 等）。
    dp = [[[-2 * 10**9] * (B + 10) for _ in range(G + 10)] for _ in range(R + 10)]
    dp[0][0][0] = 0
    ans = 0
    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                dp[i][j][k] = max(
                    dp[i][j][k],
                    dp[i - 1][j - 1][k] + red[i - 1] * green[j - 1],
                    dp[i][j - 1][k - 1] + green[j - 1] * blue[k - 1],
                    dp[i - 1][j][k - 1] + red[i - 1] * blue[k - 1],
                )
                ans = max(ans, dp[i][j][k])
    print(ans)


if __name__ == "__main__":
    # 示例：规模为 3
    main(3)