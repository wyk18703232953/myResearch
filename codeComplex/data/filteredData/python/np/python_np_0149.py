import bisect
import copy
import decimal
import fractions
import functools
import heapq
import itertools
import math
import random
import sys
from collections import Counter, deque, defaultdict
from functools import lru_cache, reduce
from heapq import heappush, heappop, heapify, heappushpop, _heappop_max, _heapify_max
from math import gcd as GCD

def _heappush_max(heap, item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap) - 1)

def _heappushpop_max(heap, item):
    if heap and item < heap[0]:
        item, heap[0] = heap[0], item
        heapq._siftup_max(heap, 0)
    return item

class Prime:
    def __init__(self, N):
        assert N <= 10**8
        self.smallest_prime_factor = [None] * (N + 1)
        for i in range(2, N + 1, 2):
            self.smallest_prime_factor[i] = 2
        n = int(N ** 0.5) + 1
        for p in range(3, n, 2):
            if self.smallest_prime_factor[p] is None:
                self.smallest_prime_factor[p] = p
                for i in range(p * p, N + 1, 2 * p):
                    if self.smallest_prime_factor[i] is None:
                        self.smallest_prime_factor[i] = p
        for p in range(n, N + 1):
            if self.smallest_prime_factor[p] is None:
                self.smallest_prime_factor[p] = p
        self.primes = [p for p in range(N + 1) if p == self.smallest_prime_factor[p]]

    def Factorize(self, N):
        assert N >= 1
        factorize = defaultdict(int)
        if N <= len(self.smallest_prime_factor) - 1:
            while N != 1:
                factorize[self.smallest_prime_factor[N]] += 1
                N //= self.smallest_prime_factor[N]
        else:
            for p in self.primes:
                while N % p == 0:
                    N //= p
                    factorize[p] += 1
                if N < p * p:
                    if N != 1:
                        factorize[N] += 1
                    break
                if N <= len(self.smallest_prime_factor) - 1:
                    while N != 1:
                        factorize[self.smallest_prime_factor[N]] += 1
                        N //= self.smallest_prime_factor[N]
                    break
            else:
                if N != 1:
                    factorize[N] += 1
        return factorize

    def Divisors(self, N):
        assert N > 0
        divisors = [1]
        for p, e in self.Factorize(N).items():
            A = [1]
            for _ in range(e):
                A.append(A[-1] * p)
            divisors = [i * j for i in divisors for j in A]
        return divisors

    def Is_Prime(self, N):
        return N == self.smallest_prime_factor[N]

    def Totient(self, N):
        for p in self.Factorize(N).keys():
            N *= p - 1
            N //= p
        return N

    def Mebius(self, N):
        fact = self.Factorize(N)
        for e in fact.values():
            if e >= 2:
                return 0
        else:
            if len(fact) % 2 == 0:
                return 1
            else:
                return -1

def main(n):
    # n 作为规模参数：
    # 使用 n 生成 N 和 Q，并构造随机测试数据 A 和查询序列。
    # 这里设：
    #   N = n
    #   Q = n
    #   A[i] 在 [1, 5*10**5] 范围内随机生成
    #   查询随机选择 [1, N] 的位置
    N = max(1, n)
    Q = max(1, n)

    MAXV = 5 * 10**5
    P = Prime(MAXV)
    mebius = [0] + [P.Mebius(i) for i in range(1, MAXV + 1)]
    cnt = [0] * (MAXV + 1)
    ans = 0

    random.seed(0)
    A = [random.randint(1, MAXV) for _ in range(N)]
    used = [False] * N

    outputs = []
    for _ in range(Q):
        q = random.randrange(N)  # 0-based index
        prime = list(P.Factorize(A[q]).keys())
        l = len(prime)
        for bit in range(1 << l):
            s = 1
            for i in range(l):
                if bit >> i & 1:
                    s *= prime[i]
            if used[q]:
                cnt[s] -= 1
                ans -= cnt[s] * mebius[s]
            else:
                ans += cnt[s] * mebius[s]
                cnt[s] += 1
        used[q] = not used[q]
        outputs.append(str(ans))

    # 按原逻辑逐行输出
    sys.stdout.write("\n".join(outputs))

if __name__ == "__main__":
    # 示例：可以在此处调整 n 以测试
    main(10)