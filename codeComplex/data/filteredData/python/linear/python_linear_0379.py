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

    def solve(self, s: str) -> str:
        s = list(s)
        n = len(s)

        res = []
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
        return ''.join(res)

@timer
def main(n: int):
    # 生成长度为 n 的测试数据，字符从 '0','1','2' 中随机选择
    chars = ['0', '1', '2']
    test_str = ''.join(random.choice(chars) for _ in range(n))

    solver = Solver()
    result = solver.solve(test_str)
    print(result)

if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)