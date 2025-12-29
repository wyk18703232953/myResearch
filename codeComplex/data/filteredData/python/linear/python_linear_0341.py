import functools
import time
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

class Solver:
    def __init__(self, n, d, x):
        self.n = n
        self.d = d
        self.x = x

    def solve(self):
        n, d, x = self.n, self.d, self.x
        ans = set()
        for i in range(n):
            for z in [-d, d]:
                y = x[i] + z
                dmin = min(abs(y - xi) for xi in x)
                if dmin == d:
                    ans.add(y)
        print(len(ans))

@timer
def main(n):
    # 根据 n 生成测试数据
    # 生成 n 个整数，范围可根据需要调整
    random.seed(0)
    d = random.randint(1, 10)
    # 保证数列中元素互不相同，且有一定间隔
    x = sorted(random.sample(range(0, 100 * n + 1), n))
    solver = Solver(n, d, x)
    solver.solve()

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可根据需要修改
    main(10)