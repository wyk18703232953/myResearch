import functools
import time
from collections import Counter

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

    def __call__(self):
        n, m = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
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

solver()()