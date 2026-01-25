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
    def __init__(self, n, d, x):
        self.n = n
        self.d = d
        self.x = x
        self.solve()

    def solve(self):
        n = self.n
        d = self.d
        x = self.x
        ans = set()
        for i in range(n):
            for z in [-d, d]:
                y = x[i] + z
                dmin = min(abs(y - xi) for xi in x)
                if dmin == d:
                    ans.add(y)
        print(len(ans))

def main(n):
    if n <= 0:
        return
    d = max(1, n // 2)
    x = [i for i in range(n)]
    solver(n, d, x)

if __name__ == "__main__":
    main(10)