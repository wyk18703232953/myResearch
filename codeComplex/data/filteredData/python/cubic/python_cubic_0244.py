import random

INF = float('inf')
mod = int(1e9) + 7

def main(n):
    """
    n 用作规模参数，这里解释为：
    r = g = b = n
    并为 R, G, B 生成长度为 n 的随机测试数据（正整数）。
    返回最大得分。
    """
    # 1. 生成规模
    r = g = b = n

    # 2. 生成测试数据（可根据需要自定义生成策略）
    #   这里使用 1..1000 的随机整数
    R = sorted(random.randint(1, 1000) for _ in range(r))
    G = sorted(random.randint(1, 1000) for _ in range(g))
    B = sorted(random.randint(1, 1000) for _ in range(b))

    # 3. 初始化 DP
    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    # 4. 递归函数保持原逻辑
    def recur(rr, gg, bb):
        if (rr + gg + bb) == rr or (rr + gg + bb) == gg or (rr + gg + bb) == bb:
            return 0
        if dp[rr][gg][bb]:
            return dp[rr][gg][bb]
        best = 0
        if rr > 0 and gg > 0:
            best = max(best, R[rr - 1] * G[gg - 1] + recur(rr - 1, gg - 1, bb))
        if rr > 0 and bb > 0:
            best = max(best, R[rr - 1] * B[bb - 1] + recur(rr - 1, gg, bb - 1))
        if bb > 0 and gg > 0:
            best = max(best, B[bb - 1] * G[gg - 1] + recur(rr, gg - 1, bb - 1))
        dp[rr][gg][bb] = best
        return best

    # 5. 返回结果（不使用输入输出）
    return recur(r, g, b)


# 示例：直接运行文件时做一次测试
if __name__ == "__main__":
    ans = main(3)
    print(ans)