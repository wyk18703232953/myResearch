import sys

squares = set([i * i for i in range(1, 4000)])
MAX_A = 10 ** 7

p = [i for i in range(MAX_A + 1)]
for i in range(1, MAX_A + 1):
    if p[i] == i:
        for sq in squares:
            v = i * sq
            if v > MAX_A:
                break
            p[v] = i


def solve_one(N, K, A):
    new = 10 ** 8  # kept to preserve original structure, though unused
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


def main(n):
    # Interpret n as total input size scale.
    # We construct T test cases, each with N elements, so that T * N ≈ n.
    if n <= 0:
        return
    T = max(1, n // 1000)
    N = max(1, n // T)
    K = min(20, max(1, N // 10))

    outputs = []
    base = 2
    for t in range(T):
        A = [base + ((i * 7 + t) % (10 ** 6)) for i in range(N)]
        outputs.append(str(solve_one(N, K, A)))
        base += 1
        if base > 1000:
            base = 2
    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main(100000)