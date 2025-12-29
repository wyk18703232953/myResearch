import functools
import time
from collections import Counter
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

    def solve(self, n, m, a):
        h = Counter()
        for ai in a:
            h[ai] = h[ai] + 1 if ai in h else 1
        days = 0
        while True:
            tot = 0
            for key, cnt in h.items():
                tot += cnt // (days + 1)
            if tot < n:
                print(days)
                return
            days += 1

def main(n):
    # 根据规模 n 生成测试数据
    # 设 m 为 O(n)，这里取 m = 2 * n，值域设为 1..n
    m = max(1, 2 * n)
    random.seed(0)
    a = [random.randint(1, n) for _ in range(m)]

    s = solver()
    s.solve(n, m, a)

if __name__ == "__main__":
    # 示例：用 n = 10 运行
    main(10)