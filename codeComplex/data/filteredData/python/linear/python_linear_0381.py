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
    def __init__(self, n, m, pairs):
        self.n = n
        self.m = m
        self.pairs = pairs

    def __call__(self):
        n = self.n
        m = self.m
        y = 0
        for i in range(m):
            x, d = self.pairs[i]
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
        # print(f'{y:.9f}')
        pass

def main(n):
    # 输入规模含义：
    # n 为原问题中的 n，同时设 m = n
    # 构造 m 组 (x, d)
    # 确定性构造：x = i, d = i - n//2 （i 从 1 到 m）
    if n <= 0:
        return
    m = n
    pairs = [(i, i - n // 2) for i in range(1, m + 1)]
    s = solver(n, m, pairs)
    s()

if __name__ == "__main__":
    main(10)