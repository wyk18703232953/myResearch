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
    def __init__(self, n, m, pairs):
        self.n = n
        self.m = m
        self.pairs = pairs

    def __call__(self):
        n, m = self.n, self.m
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
        return y

def generate_input(n):
    if n < 1:
        n = 1
    m = n
    pairs = []
    for i in range(m):
        x = (i * 3) - n
        d = (i % 5) - 2
        pairs.append((x, d))
    return n, m, pairs

@timer
def main(n):
    n_val, m_val, pairs = generate_input(n)
    s = solver(n_val, m_val, pairs)
    return s()

if __name__ == "__main__":
    main(10)