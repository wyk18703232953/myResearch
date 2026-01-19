import sys

mod = 10**9 + 7

def main(n):
    # Interpret n as the number of songs; total time t is chosen deterministically.
    if n <= 0:
        print(0)
        return

    # Deterministic construction of song durations and genres.
    # duration: i + 1, genre: i % 3 for i in 0..n-1
    a = []
    total_duration = 0
    for i in range(n):
        time = i + 1
        genre = i % 3
        a.append((time, genre))
        total_duration += time

    # Choose target duration t as total_duration // 2 for a non-trivial subset.
    t = total_duration // 2

    dp = [[0 for _ in range(3)] for _ in range(1 << n)]
    for i in range(n):
        dp[1 << i][a[i][1]] = 1

    for mask_state in range(1 << n):
        for last_genre in range(3):
            if dp[mask_state][last_genre] == 0:
                continue
            mask = 1
            for k in range(n):
                if (mask_state & mask) or a[k][1] == last_genre:
                    mask <<= 1
                    continue
                new_state = mask_state | mask
                g = a[k][1]
                dp[new_state][g] = (dp[new_state][g] + dp[mask_state][last_genre]) % mod
                mask <<= 1

    ans = 0
    for mask_state in range(1 << n):
        mask = 1
        duration = 0
        for j in range(n):
            if mask_state & mask:
                duration += a[j][0]
            mask <<= 1
        if duration == t:
            ans = (ans + sum(dp[mask_state])) % mod

    print(ans)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments.
    main(5)