import math

MOD = 10**9 + 7

squares = set(i * i for i in range(1, 4000))

p = [i for i in range(10**7 + 1)]
for i in range(1, 10**7 + 1):
    if p[i] == i:
        for sq in squares:
            if i * sq > 10**7:
                break
            p[i * sq] = i

def solve(N, K, A):
    A = [p[A[i]] for i in range(N)]
    dp = [N] * (K + 1)
    dp[0] = 0
    used = [set()] * (K + 1)
    for i in range(N):
        for j in range(K, -1, -1):
            if dp[j] == N:
                continue
            if A[i] in used[j]:
                if j < K and dp[j + 1] > dp[j]:
                    dp[j + 1] = dp[j]
                    used[j + 1] = used[j]
                dp[j] += 1
                used[j] = set([A[i]])

            else:
                used[j].add(A[i])
    return min(dp) + 1

def generate_testcase(n):
    T = max(1, n)
    testcases = []
    for t in range(1, T + 1):
        N = max(1, t)
        K = min(N, (t % (N + 1)))
        if K == 0:
            K = min(1, N)
        A = [((i + t) * (i + 1)) % (10**7) + 1 for i in range(N)]
        testcases.append((N, K, A))
    return testcases

def main(n):
    testcases = generate_testcase(n)
    results = []
    for N, K, A in testcases:
        results.append(solve(N, K, A))
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(3)