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

class Solver:
    # @timer
    def __init__(self, n):
        self.n = n

    def __call__(self):
        n = self.n
        minv = n + 1
        mini = n
        for l in range(1, n + 1):
            v = l + (n + l - 1) // l
            if v < minv:
                minv = v
                mini = l

        ref = [i + 1 for i in range(n)]
        l = mini
        res = []
        p = n - 1
        while p >= 0:
            pp = max(0, p - l + 1)
            res.extend(ref[pp:p + 1])
            p = pp - 1
        # print(' '.join(map(str, res)))
        pass

def main(n):
    # 这里根据 n 生成测试数据：原题只需要一个整数 n
    # 若后续扩展为复杂数据，可在此构造
    Solver(n)()

if __name__ == "__main__":
    # 示例：可修改为任意规模 n 做测试
    main(10)