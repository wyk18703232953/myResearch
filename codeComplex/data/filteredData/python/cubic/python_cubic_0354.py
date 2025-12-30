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
            num //= p
        if c % 2 == 1:
            dv.append(p)
        if num < p * p:
            break

    for x in dv:
        num *= x

    cache[key] = num
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
                    used[j + 1] = dict(used[j])
                dp[j] += 1
                used[j] = {}
            used[j][a] = 1
    return min(dp)


def main(n):
    """
    n: 规模参数，用于生成测试数据。
       这里简单设定：
       - 测试组数 T = 1
       - N = n
       - K = max(1, n // 10)
       - A 为长度 N 的数组，元素为 1..10^6 的简单构造数据
    """
    import random

    random.seed(0)

    T = 1
    N = max(1, n)
    K = max(1, n // 10)
    # 生成测试数组：从 1 到 10^6 随机取数
    A = [random.randint(1, 10**6) for _ in range(N)]

    # 按原逻辑，仅一组测试
    ans = solve_one(N, K, A)
    print(ans)


if __name__ == "__main__":
    # 示例：以 n = 100 运行
    main(100)