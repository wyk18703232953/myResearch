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
    def __init__(self):
        pass

    def solve(self, n, m, pairs):
        y = 0
        for x, d in pairs:
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
        print(f"{y:.9f}")

@timer
def main(n):
    # 根据规模 n 生成测试数据
    # 这里令 m 与 n 同级，可按需调整生成规则
    m = max(1, n)  # 至少一组数据
    # 生成 m 对 (x, d)
    # x: [-10^6, 10^6], d: [-10^6, 10^6]
    pairs = []
    for _ in range(m):
        x = random.randint(-10**6, 10**6)
        d = random.randint(-10**6, 10**6)
        pairs.append((x, d))

    solver = Solver()
    solver.solve(n, m, pairs)

if __name__ == "__main__":
    # 示例：调用 main(1000)
    main(1000)