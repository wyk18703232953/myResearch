import sys

def main(n):
    mod = 10**9 + 7

    # Deterministic generation of n and T and people data.
    # Interpret input structure as:
    # first line: n T
    # next n lines: duration genre(1..3)
    #
    # Here we map the user-provided n to:
    # - number of people = n
    # - target T = n * (n + 1) // 2 (sum of 1..n)
    # - durations: 1..n
    # - genres: cycle through 1,2,3
    T = n * (n + 1) // 2
    peo = [[i + 1, (i % 3) + 1] for i in range(n)]

    y = 1 << n
    dp = [[0] * 3 for _ in range(y)]

    for ind, person in enumerate(peo):
        person[1] -= 1  # convert genre 1..3 to 0..2
        dp[1 << ind][person[1]] = 1

    for mask_state in range(y):
        for last_genre in range(3):
            if not dp[mask_state][last_genre]:
                continue
            mask = 1
            for k in range(n):
                if mask_state & mask or peo[k][1] == last_genre:
                    mask <<= 1
                    continue
                dp[mask_state | mask][peo[k][1]] = (dp[mask_state | mask][peo[k][1]] + dp[mask_state][last_genre]) % mod
                mask <<= 1

    ans = 0
    for mask_state in range(y):
        total_duration = 0
        mask = 1
        for j in range(n):
            if mask_state & mask:
                total_duration += peo[j][0]
            mask <<= 1
        if total_duration == T:
            ans = (ans + sum(dp[mask_state])) % mod

    print(ans)


if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(5)