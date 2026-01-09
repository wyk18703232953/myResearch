def main(n):
    # n: input scale = length of array A
    if n <= 0:
        # print(0)
        pass
        return

    # deterministic construction of A based on n
    # mix of small and growing values to exercise merging behavior
    A = [(i ^ (i // 2)) % (max(1, n // 3)) + (i % 5) for i in range(n)]

    N = n
    dp = [[False for _ in range(N)] for _ in range(N)]
    for l in range(N):
        tmp = [A[l]]
        dp[l][l] = True
        for r in range(l + 1, N):
            val = A[r]
            while tmp and tmp[-1] == val:
                val = tmp[-1] + 1
                tmp.pop()
            tmp.append(val)
            if len(tmp) == 1:
                dp[l][r] = True

    res = [i for i in range(N + 1)]
    for r in range(1, N + 1):
        for l in range(1, r + 1):
            if dp[l - 1][r - 1]:
                res[r] = min(res[r], 1 + res[l - 1])

    # print(res[N])
    pass
if __name__ == "__main__":
    # example deterministic call
    main(10)