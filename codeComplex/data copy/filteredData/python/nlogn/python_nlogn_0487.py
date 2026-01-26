import functools
import time
from collections import Counter

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

    def __call__(self, n, m, a):
        h = Counter()
        for ai in a:
            h[ai] = h[ai] + 1 if ai in h else 1
        days = 0
        while True:
            tot = 0
            for key, cnt in h.items():
                tot += cnt // (days + 1)
            if tot < n:
                return days
            days += 1

def main(n):
    if n < 1:
        n = 1
    m = 2 * n
    a = [(i % (n // 2 + 1)) + 1 for i in range(m)]
    s = solver()
    result = s(n, m, a)
    # print(result)
    pass
if __name__ == "__main__":
    main(1000)