import random

def get_prime(limit):
    res = []
    for i in range(2, limit):
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
            num //= p
        if c % 2 == 1:
            dv.append(p)
        if num < p * p:
            break
    for x in dv:
        num *= x
    return num


def solve_one(N, K, A):
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
    # n 作为规模参数：生成 n 组测试
    t = n
    random.seed(1)
    for _ in range(t):
        # 为每组测试生成 N, K, A
        N = max(1, n)          # 可按需求调整规模策略
        K = min(10, N - 1) if N > 1 else 0
        A = [random.randint(1, 10**6) for _ in range(N)]
        ans = solve_one(N, K, A)
        print(ans)


if __name__ == "__main__":
    main(3)