from collections import deque
import random

INF = 250005

def solve_instance(n, m, lesson, days_strs):
    # 转换 days_strs 为 days 列表（每行存放开课的节次下标，从 1 开始）
    days = [[] for _ in range(n)]
    for i in range(n):
        s = days_strs[i]
        for j in range(m):
            if s[j] == "1":
                days[i].append(j + 1)

    # m_cost[i][j]: 第 i 天选 j 节课时，最小的连续区间长度代价
    m_cost = [[INF for _ in range(lesson + 2)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(lesson + 1):
            if j <= len(days[i]):
                if j == len(days[i]):
                    m_cost[i][j] = 0
                else:
                    best = INF
                    for k in range(0, j + 1):
                        left = days[i][0 + k]
                        right = days[i][-1 * max(1, 1 + (j - k))]
                        best = min(best, right - left + 1)
                    m_cost[i][j] = best

    # dp[i][j]: 前 i+1 天（0..i），总共选 j 节课时的最小代价
    dp = [[INF for _ in range(lesson + 2)] for _ in range(n + 1)]

    for j in range(lesson + 1):
        dp[0][j] = m_cost[0][j]

    for i in range(1, n):
        for j in range(lesson + 1):
            best = INF
            for k in range(j + 1):
                best = min(best, dp[i - 1][j - k] + m_cost[i][k])
            dp[i][j] = best

    return min(dp[n - 1][:lesson + 1])


def main(n):
    # 规模 n 为天数，其他参数根据 n 构造
    # 这里给出一种简单的生成策略，可根据需要调整：
    #
    # m: 每天的最大节次数
    # lesson: 希望总共选择的节次数上限
    #
    # 生成 days_strs：长度为 n，每个是长度为 m 的 0/1 串

    random.seed(0)

    # 设置 m 与 lesson 与 n 同阶
    m = max(1, n * 2)           # 比如 m = 2n
    lesson = min(m, max(1, n))  # lesson 不超过 m

    days_strs = []
    for _ in range(n):
        # 每天随机生成一个 0/1 串，1 的个数随机
        num_ones = random.randint(0, m)
        positions = random.sample(range(m), num_ones)
        s_list = ['0'] * m
        for pos in positions:
            s_list[pos] = '1'
        days_strs.append(''.join(s_list))

    ans = solve_instance(n, m, lesson, days_strs)
    print(ans)


# 示例调用：
# main(5)