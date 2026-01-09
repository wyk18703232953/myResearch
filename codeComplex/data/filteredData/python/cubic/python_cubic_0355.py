def get_prime(n):
    res = []
    for i in range(2, n):
        is_prime = True
        for x in res:
            if i % x == 0:
                is_prime = False
                break
        if is_prime:
            res.append(i)
    return res


prime = get_prime(3162)


def get_mask(num):
    dv = []
    for p in prime:
        c = 0
        while num % p == 0:
            c += 1
            num = num // p
        if c % 2 == 1:
            dv.append(p)
        if num < p * p:
            break

    for x in dv:
        num *= x

    return num


def main(n):
    # Interpret n as both number of test cases and base size
    T = n if n > 0 else 1
    results = []

    for t in range(T):
        # For each test case, define N and K deterministically from t and n
        # N grows with n and t, K is bounded by log scale of N
        N = max(1, n + t)
        K = max(0, min(10, N // 5))

        # Generate array A of length N, values constructed deterministically
        # Use a simple pattern that gives composite and non-trivial factorization
        A = [i * i + 2 * i + 3 for i in range(1, N + 1)]

        dp = [N] * (K + 1)
        dp[0] = 1
        used = [{} for _ in range(K + 1)]
        for a in A:
            a = get_mask(a)
            for j in range(K, -1, -1):
                if dp[j] == N:
                    continue
                if a in used[j]:
                    if j < K and dp[j + 1] > dp[j]:
                        dp[j + 1] = dp[j]
                        used[j + 1] = dict(used[j])
                    dp[j] += 1
                    used[j] = {}
                used[j][a] = 1
        results.append(min(dp))

    # Aggregate output to keep behavior deterministic
    # (e.g., print each result on a new line)
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(5)