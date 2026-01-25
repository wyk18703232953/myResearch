import math
import bisect
from collections import defaultdict as dd
from collections import Counter

mod = 1000000007

def sieve(n):
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime

def main(n):
    if n < 3:
        print("NO")
        return

    # 确定性生成 k，规模与 n 成比例
    k = max(1, n // 10)

    all_prime_flags = sieve(n)

    primes = []
    for i in range(1, len(all_prime_flags)):
        if all_prime_flags[i]:
            primes.append(i)

    s = Counter(primes)

    res = 0
    for i in range(len(primes) - 1):
        toCheck = primes[i] + primes[i + 1] + 1
        if toCheck in s:
            res += 1

    if res >= k:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    # 示例调用，可按需修改 n 以进行规模实验
    main(1000)