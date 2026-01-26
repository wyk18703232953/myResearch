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
    def __init__(self):
        pass

    def solve_string(self, s):
        s = list(s)
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
        return ''.join(map(str, res))

def main(n):
    # 生成长度为 n 的确定性字符串，只包含 '0','1','2'
    # 使用 i % 3 来决定字符
    chars = ['0', '1', '2']
    s = ''.join(chars[i % 3] for i in range(n))
    sol = solver()
    result = sol.solve_string(s)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)