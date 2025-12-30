import math
import random
from collections import defaultdict


def main(n):
    """
    n: number of players
    自动生成测试数据并运行原逻辑：
    - k: 每人手牌上限（随机）
    - cards: n * k 张牌
    - fav: n 个玩家喜爱的牌
    - h: 0..k 的得分表
    """
    # 1. 生成规模相关参数
    # 适当限制 k，避免 n 大时复杂度过高
    k = max(1, min(5, n))  # 可按需要调整规模策略

    # 2. 构造测试数据
    # 设 distinct card values 数量为 m
    m = max(1, min(5 * n, 10 * n))  # 卡牌种类
    # 所有可能牌值范围 [1, m]
    card_values = list(range(1, m + 1))

    # cards: n * k 张牌，随机分布
    cards = [random.choice(card_values) for _ in range(n * k)]

    # fav: 每位玩家一个喜爱的牌，范围也在 card_values 中
    fav = [random.choice(card_values) for _ in range(n)]

    # h: 手中 0..k 张最爱牌对应得分；h[0] = 0
    # 这里令 h[hand] 为一个不下降的随机序列，符合“张数越多得分不低”这一常见设定
    h = [0]
    cur = 0
    for _ in range(k):
        cur += random.randint(0, 10)
        h.append(cur)

    # 3. 原逻辑实现
    cards_cnt = defaultdict(int)
    for val in cards:
        cards_cnt[val] += 1

    players_fav_cnt = defaultdict(int)
    for val in fav:
        players_fav_cnt[val] += 1

    # dp[a][b] - a players, b favourite cards (in total)
    # 注意上界：b 最大可能为 k * a
    max_b = k * n + k
    dp = [[0 for _ in range(max_b + 1)] for _ in range(n + 1)]

    for p in range(n):
        for c in range(k * n + 1):
            base = dp[p][c]
            for hand in range(k + 1):
                if c + hand > max_b:
                    break
                val = base + h[hand]
                if val > dp[p + 1][c + hand]:
                    dp[p + 1][c + hand] = val

    res = 0
    for f in players_fav_cnt:
        a = players_fav_cnt[f]
        b = cards_cnt[f]
        if b > max_b:
            b = max_b
        res += dp[a][b]

    print(res)


if __name__ == '__main__':
    # 示例：运行 n = 5
    main(5)