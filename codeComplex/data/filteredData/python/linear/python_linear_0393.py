import functools
import time
import random

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        stime = time.perf_counter()
        res = func(*args, **kwargs)
        elapsed = time.perf_counter() - stime
        print(f"{func.__name__} in {elapsed:.4f} secs")
        return res
    return wrapper

class solver:
    # @timer
    def __init__(self):
        pass

    def __call__(self, n, a):
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
        print(res)

def main(n):
    # 生成长度为 n 的测试数据 a，这里使用 [1, 2, ..., n]
    # 如需不同策略，可改为随机：random.randint(0, MOD-1) 等
    a = [i + 1 for i in range(n)]
    solver()(n, a)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)