import sys
from collections import defaultdict
import random


class Prime:
    def __init__(self, N):
        assert N <= 10 ** 8
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
    # - N: 数组大小
    # - Q: 操作次数
    # 这里设置 N = n, Q = n，可以根据需要调整。
    N = n
    Q = n

    MAXV = 5 * 10 ** 5
    P = Prime(MAXV)
    mebius = [0] + [P.Mebius(i) for i in range(1, MAXV + 1)]
    cnt = [0] * (MAXV + 1)
    ans = 0

    # 生成测试数据：
    # A[i] 为 [1, MAXV] 内的随机数，保证可被预处理范围覆盖
    random.seed(0)
    A = [random.randint(1, MAXV) for _ in range(N)]

    # Q 次随机查询，索引在 [0, N-1]
    queries = [random.randint(0, N - 1) for _ in range(Q)]

    used = [False] * N

    out_lines = []
    for q in queries:
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
        out_lines.append(str(ans))

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    # 示例：使用 n=10 运行
    main(10)