def solve(N, S, C):
    dp = [float('inf')] * N
    for i in range(1, N):
        for j in range(i):
            if S[j] < S[i]:
                dp[i] = min(dp[i], C[j] + C[i])

    dp2 = [float('inf')] * N
    for i in range(N - 1, 0, -1):
        for j in range(i + 1, N, 1):
            if S[i] < S[j]:
                dp2[j] = min(dp2[j], dp[i] + C[j])

    ans = min(dp2)
    if ans == float('inf'):
        return -1
    return ans

def main(n):
    N = n
    S = [i % 10 for i in range(N)]
    C = [i % 7 + 1 for i in range(N)]
    result = solve(N, S, C)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)