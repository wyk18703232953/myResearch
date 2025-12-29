import random

def main(n):
    # 规模参数：n 行，m 列，最多可删 k 个 '1'
    # 这里简单设置 m、k 为 n 的函数，也可按需要修改
    m = max(1, n)          # 列数
    k = max(0, n // 2)     # 可删除的 '1' 总数上限

    # 3. 生成测试数据：随机 0/1 字符串
    DATA = []
    for _ in range(n):
        # 随机生成一行 0/1 串
        row = ''.join(random.choice('01') for _ in range(m))
        DATA.append(row)

    INF = 1 << 60
    # dp[day][used_cost]
    dp = [[INF] * (k + 10) for _ in range(n + 10)]
    dp[0][0] = 0

    # COST[day][x]：第 day 行在删除 x 个 '1' 时，使该行剩下的 '1' 被包含的最小区间长度
    COST = [[INF] * (k + 10) for _ in range(n + 10)]

    for i, string in enumerate(DATA):
        stack = [idx for idx, ch in enumerate(string) if ch == '1']
        L = len(stack)
        # 删除 j 个 '1'
        for j in range(k + 10):
            if j >= L:
                # 全删完，不需要区间
                COST[i + 1][j] = 0
            else:
                best = INF
                # 保留 L - j 个连续的 '1'
                for pos in range(j + 1):
                    l = pos
                    r = pos + L - 1 - j
                    best = min(best, stack[r] - stack[l] + 1)
                COST[i + 1][j] = best

    for day in range(1, n + 1):
        for used_cost in range(k + 1):
            best = INF
            for prev_cost in range(used_cost + 1):
                cur = dp[day - 1][prev_cost] + COST[day][used_cost - prev_cost]
                if cur < best:
                    best = cur
            dp[day][used_cost] = best

    ans = min(dp[n][used_cost] for used_cost in range(k + 1))
    print(ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)