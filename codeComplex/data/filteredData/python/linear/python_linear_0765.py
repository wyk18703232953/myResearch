def main(n):
    import collections
    import math

    mod = (10 ** 9) + 7

    # Deterministic data generation:
    # n: number of elements
    # q: number of queries (choose q = n for scalability)
    # a: permutation-like sequence with a clear maximum at the end
    if n < 2:
        n = 2
    q = n

    # Generate array a of length n with maximum at the end and all distinct
    # Example: [1, 2, ..., n]
    a = list(range(1, n + 1))

    # Precompute gcd and isprime just to keep structure; not used in core logic.
    def GCD(x, y):
        while y:
            x, y = y, x % y
        return x

    def isprime(x):
        if x == 1:
            return False
        elif x < 4:
            return True
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    g = max(a)
    d = collections.deque(a)
    f = 0
    an1 = []

    # Simulate the pairwise comparison process until the maximum reaches front
    while d[0] != g:
        f += 1
        x = d.popleft()
        y = d.popleft()
        an1.append(str(x) + " " + str(y))
        if y == g:
            d.appendleft(y)
            d.append(x)
            break
        if x < y:
            d.appendleft(y)
            d.append(x)

        else:
            d.appendleft(x)
            d.append(y)

    # After stabilization, record resulting order
    r = []
    for _ in range(n):
        r.append(str(d.popleft()))

    # Deterministic queries: 1, 2, ..., q
    queries = list(range(1, q + 1))

    ans = []
    for b in queries:
        if b <= f:
            ans.append(an1[b - 1])

        else:
            bb = b - f
            bb -= 1
            bb %= (n - 1)
            ans.append(r[0] + " " + r[bb + 1])

    # For complexity experiments, we return the answers instead of printing
    return ans


if __name__ == "__main__":
    # Example deterministic call for testing / benchmarking
    res = main(10)
    for line in res:
        # print(line)
        pass