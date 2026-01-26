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
    def __init__(self):
        n, m = map(int, input().strip().split())
        segs = list()
        for i in range(m):
            segs.append(list(map(int, input().strip().split())))
        
        def calc(s, segs):
            res = 0
            for x in segs:
                ones = sum(s[x[0]:x[1] + 1])
                res += ones * (x[1] - x[0] + 1 - ones)
            return res

        s1 = [0 for i in range(n)]
        s2 = [1 for i in range(n)]
        for i in range(n):
            if i % 2 == 0:
                s1[i] = 1
                s2[i] = 0

        ans = s1 if calc(s1, segs) > calc(s2, segs) else s2
        print(''.join(map(str, ans)))
        
solver()