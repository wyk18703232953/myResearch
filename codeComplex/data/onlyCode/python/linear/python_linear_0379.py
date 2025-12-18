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
        s = list(input().strip())
        n = len(s)

        res = list()
        p = n - 1        
        ones = 0
        zeros = 0
        while p >= 0:
            if s[p] == '0':
                zeros += 1
            elif s[p] == '1':
                ones += 1
            elif s[p] == '2':
                res.extend(['0'] * zeros)
                res.append('2')
                zeros = 0
            p -= 1
        res.extend(['1'] * ones)
        res.extend(['0'] * zeros)
        res.reverse()
        print(''.join(map(str, res)))

solver()()