import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

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

N = int(input())
S = get_ints()
C = get_ints()

print(solve(N, S, C))
