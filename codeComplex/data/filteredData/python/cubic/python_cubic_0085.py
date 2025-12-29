import random

def main(n):
    """
    n: problem scale, used here as the value of n in the original problem.
       We also choose k based on n and generate random test data.
    """
    # 1. Generate parameters
    k = max(1, n // 3)  # a reasonable k relative to n

    # values a[i] (card) and b[i] (fav) are in [1, 1e5], as implied by tot arrays
    MAX_VAL = 10**5

    # 2. Generate test data
    card = [random.randint(1, MAX_VAL) for _ in range(n)]
    fav = [random.randint(1, MAX_VAL) for _ in range(n)]

    # joy array of length k+1 (originally read as [0] + list(map(int,input().split())))
    # joy[0..k]; joy[0] must be 0 (as in original code).
    joy = [0] + [random.randint(0, 10**4) for _ in range(k)]

    # 3. Core logic (same as original main(), but using generated data)
    dp = [[0] * (n * k + 1) for _ in range(n + 1)]

    # fill dp[1][*]
    for i in range(len(joy)):
        dp[1][i] = joy[i]
    for i in range(len(joy), n * k + 1):
        dp[1][i] = joy[-1]

    for i in range(2, n + 1):
        for j in range(1, n * k + 1):
            # number of increments kk used at this level, up to k, and not exceeding j
            limit = min(k, j)
            best = dp[i][j]  # current value
            base_prev = dp[i - 1]
            base_first = dp[1]
            for kk in range(limit + 1):
                val = base_prev[j - kk] + base_first[kk]
                if val > best:
                    best = val
            dp[i][j] = best

    tot = [0] * (MAX_VAL + 1)
    for x in card:
        tot[x] += 1

    tot1 = [0] * (MAX_VAL + 1)
    for x in fav:
        tot1[x] += 1

    ans = 0
    for i in range(MAX_VAL + 1):
        cnt_fav = tot1[i]
        cnt_card = tot[i]
        if cnt_fav <= n and cnt_card <= n * k:
            ans += dp[cnt_fav][cnt_card]

    print(ans)


if __name__ == "__main__":
    # Example: run with n = 5; adjust as needed
    main(5)