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
cache = {}


def get_mask(num):
    key = num
    if key in cache:
        return cache[key]
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
    cache[key] = num
    return num


def run_single_case(N, K, A):
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
                    used[j + 1] = used[j].copy()
                dp[j] += 1
                used[j] = {}
            used[j][a] = 1
    return min(dp)


def main(n):
    T = max(1, n // 5)
    results = []
    for t in range(T):
        N = max(1, n)
        K = max(0, n // 10)
        A = [i * (i % 7 + 1) + (t + 1) for i in range(1, N + 1)]
        res = run_single_case(N, K, A)
        results.append(res)
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(1000)