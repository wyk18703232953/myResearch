import random

class sieve:
    def __init__(self, n):
        self.n = n
        self.sv = [1] * (n + 1)
        self.sv[0] = 0
        self.sv[1] = 0
        for i in range(2, n + 1):
            if self.sv[i]:
                for j in range(i * 2, n + 1, i):
                    self.sv[j] = 0

    def isprime(self, x):
        if x > self.n:
            return False
        return self.sv[x] == 1

    def factorize(self, x):
        res = []
        for i in range(2, int(x ** 0.5) + 1):
            if self.sv[i]:
                while x % i == 0:
                    x //= i
                    res.append(i)
        if x != 1:
            res.append(x)
        return res

    def modlcm(self, a, mod):
        res = [0] * (self.n + 1)
        ex = set()
        for i in range(len(a)):
            f = self.factorize(a[i])
            for j in f:
                if j > self.n:
                    ex.add(j)
                    continue
                res[j] = max(f.count(j), res[j])
        rres = 1
        for i in range(self.n + 1):
            if res[i] != 0:
                rres *= pow(i, res[i], mod)
                rres %= mod
        for i in ex:
            rres *= i
            rres %= mod
        return rres


def solve_one_case(n, k, a, sv):
    # normalize a[i] by removing squared prime factors
    for i in range(n):
        x = a[i]
        q = sv.factorize(x)
        s = [1]
        while len(q):
            y = q.pop()
            if y == s[-1]:
                s.pop()
                a[i] //= y ** 2
            else:
                s.append(y)

    s = [set() for _ in range(k + 1)]
    dp = [n] * (k + 1)
    dp[0] = 0

    for i in range(n):
        for j in range(k, -1, -1):
            if dp[j] == n:
                continue
            if a[i] in s[j]:
                if j + 1 <= k and dp[j + 1] > dp[j]:
                    dp[j + 1] = dp[j]
                    s[j + 1] = s[j]
                dp[j] += 1
                s[j] = set()
                s[j].add(a[i])
            else:
                s[j].add(a[i])

    for j in range(k + 1):
        dp[j] += len(s[j]) > 0
    return min(dp)


def main(n):
    """
    n: problem scale parameter.
       We generate one test case with:
       - array length = n
       - k chosen as max(1, n // 5)
       - array values in [1, 10^4]
    """
    max_val = 10 ** 4
    sv = sieve(max_val)

    # generate test data
    length = n
    k = max(1, n // 5)
    a = [random.randint(1, max_val) for _ in range(length)]

    ans = solve_one_case(length, k, a, sv)
    print(ans)


if __name__ == "__main__":
    # example: run with scale 10
    main(10)