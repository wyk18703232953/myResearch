from collections import Counter

mod = 1000000007


def sieve(n):
    prime = [True for _ in range(n + 1)]
    if n >= 0:
        prime[0] = False
    if n >= 1:
        prime[1] = False

    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime


def main(n):
    """
    n: 规模参数，用来生成测试数据。
       这里约定：
       - 实际判断的上界也为 n
       - k 取为 n//10（至少为 1），可根据需要调整生成策略
    """
    if n < 2:
        # 没有质数，直接输出 NO
        # print("NO")
        pass
        return

    # 根据 n 生成 k（可按需求更改）
    k = max(1, n // 10)

    all_prime = sieve(n)

    primes = [i for i in range(2, n + 1) if all_prime[i]]

    s = Counter(primes)

    res = 0
    for i in range(len(primes) - 1):
        toCheck = primes[i] + primes[i + 1] + 1
        if toCheck in s:
            res += 1

    if res >= k:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例：可修改为任意规模 n 进行测试
    main(100)