import math
from collections import defaultdict


def main(n):
    # n: number of players
    if n <= 0:
        # print(0)
        pass
        return

    # scale k with n to keep complexity meaningful
    k = max(1, n // 2)

    # deterministic construction of cards and favourites
    # value domain size m
    m = max(1, n // 3 + 1)

    cards = [(i % m) + 1 for i in range(k * n)]
    fav = [((i * 2) % m) + 1 for i in range(n)]

    # h[hand] values for 0..k
    h = [0] + [i * i for i in range(1, k + 1)]

    cards_cnt = defaultdict(int)
    for val in cards:
        cards_cnt[val] += 1

    players_fav_cnt = defaultdict(int)
    for val in fav:
        players_fav_cnt[val] += 1

    dp = [[0 for _ in range(k * n + k + 1)] for _ in range(n + 1)]
    for p in range(n):
        for c in range(k * n + 1):
            base = dp[p][c]
            # unrolled inner loop for clarity with deterministic h
            for hand in range(k + 1):
                nc = c + hand
                dp_val = base + h[hand]
                if dp[p + 1][nc] < dp_val:
                    dp[p + 1][nc] = dp_val

    res = 0
    for f in players_fav_cnt:
        res += dp[players_fav_cnt[f]][cards_cnt[f]]

    # print(res)
    pass
if __name__ == "__main__":
    main(10)