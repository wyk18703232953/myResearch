def main(n):
    # Map n to three array sizes, each at most 200 (due to dp size 201^3)
    n1 = min(n, 200)
    n2 = min(max(n - 50, 0), 200)
    n3 = min(max(n - 100, 0), 200)

    # Ensure at least 1 when n > 0
    if n > 0:
        if n1 == 0:
            n1 = 1
        if n2 == 0:
            n2 = 1
        if n3 == 0:
            n3 = 1

    # Deterministic generation of arrays based on sizes
    ar = [(i * 2 + 1) for i in range(n1)]
    br = [(i * 3 + 2) for i in range(n2)]
    cr = [(i * 5 + 3) for i in range(n3)]

    ar.sort()
    br.sort()
    cr.sort()

    MAX_DIM = 200
    # dp dimension fixed to 201, original code assumes <=200
    dp = [[[0 for _ in range(MAX_DIM + 1)] for _ in range(MAX_DIM + 1)] for _ in range(MAX_DIM + 1)]

    for i in range(n1 + 1):
        for j in range(n2 + 1):
            for k in range(n3 + 1):
                val = dp[i][j][k]
                if i and j:
                    tmp = dp[i - 1][j - 1][k] + ar[i - 1] * br[j - 1]
                    if tmp > val:
                        val = tmp
                if i and k:
                    tmp = dp[i - 1][j][k - 1] + ar[i - 1] * cr[k - 1]
                    if tmp > val:
                        val = tmp
                if k and j:
                    tmp = dp[i][j - 1][k - 1] + cr[k - 1] * br[j - 1]
                    if tmp > val:
                        val = tmp
                dp[i][j][k] = val

    # print(dp[n1][n2][n3])
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to scale input size
    main(50)