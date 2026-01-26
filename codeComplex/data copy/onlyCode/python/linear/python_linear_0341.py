import functools
import time

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
        n, d = map(int, input().strip().split())
        x = list(map(int, input().strip().split()))
        ans = set()
        for i in range(n):
            for z in [-d, d]:
                y = x[i] + z
                dmin = min(abs(y - xi) for xi in x)
                if dmin == d:
                    ans.add(y)
        print(len(ans))

solver()