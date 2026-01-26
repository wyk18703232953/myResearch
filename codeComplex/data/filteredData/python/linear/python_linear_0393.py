import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        stime = time.perf_counter()
        res = func(*args, **kwargs)
        elapsed = time.perf_counter() - stime
        # print(f"{func.__name__} in {elapsed:.4f} secs")
        pass
        return res
    return wrapper

class solver:
    # @timer
    def __init__(self):
        pass

    def solve(self, n, a):
        MOD = 998244353
        N = 1000007
        pow2 = [0] * N

        pow2[0] = 1
        for i in range(n):
            pow2[i + 1] = (2 * pow2[i]) % MOD

        res = 0
        for i in range(1, n):
            tmp = (a[i - 1] * (n + 2 - i)) % MOD
            res += (pow2[n - 1 - i] * tmp) % MOD
            res %= MOD
        res += a[n - 1]
        res %= MOD
        # print(res)
        pass
        return res

def main(n):
    if n <= 0:
        return None
    a = [i % 100000 for i in range(1, n + 1)]
    s = solver()
    return s.solve(n, a)

if __name__ == "__main__":
    main(10)