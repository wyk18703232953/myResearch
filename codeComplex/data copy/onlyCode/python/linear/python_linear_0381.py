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
        pass

    def __call__(self):
        n, m = map(int, input().strip().split())

        y = 0
        for _ in range(m):
            x, d = map(int, input().strip().split())
            if d >= 0:  
                y += d * (n - 1) * n // 2
            else:
                if n % 2 != 0:
                    l = (n - 1) // 2
                    y += d * l * (l + 1)
                else:
                    l = n // 2
                    y += d * (l * (l + 1) - l)
            y += x * n
        y /= n
        print(f'{y:.9f}')

solver()()