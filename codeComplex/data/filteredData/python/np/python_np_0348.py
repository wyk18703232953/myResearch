import string
from math import inf
from functools import lru_cache

MOD = int(1e9 + 7)


def main(n):
    # n controls number of songs, time limit t is deterministically derived
    if n <= 0:
        print(0)
        return

    # generate deterministic songs: [time, genre]
    # time starts from 1; genre cycles through 0,1,2
    songs = [[i + 1, (i % 3)] for i in range(n)]

    # set target time as sum of first min(3, n) song times
    k = 3 if n >= 3 else n
    t = k * (k + 1) // 2

    result = 0
    dp = [[0, 0, 0] for _ in range(1 << n)]

    for ind, it in enumerate(songs):
        dp[1 << ind][it[1]] = 1

    for mask in range(1, 1 << n):
        for genre in range(3):
            for nsng, sng in enumerate(songs):
                if sng[1] != genre and ((mask >> nsng) & 1) == 0:
                    dp[mask | (1 << nsng)][sng[1]] += dp[mask][genre]

            sm = 0
            for ind, it in enumerate(reversed(bin(mask)[2:])):
                if it == '1':
                    sm += songs[ind][0]
            if sm == t:
                result += dp[mask][genre]
                result %= MOD

    print(result)


if __name__ == "__main__":
    main(5)