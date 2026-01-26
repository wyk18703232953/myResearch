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

def generate_segments(n):
    if n <= 0:
        return []
    segs = []
    segs.append([0, n - 1])
    if n > 1:
        step = max(1, n // 4)
        for i in range(0, n - 1, step):
            l = i
            r = min(n - 1, i + step)
            if l <= r:
                segs.append([l, r])
    return segs

def calc(s, segs):
    res = 0
    for x in segs:
        l, r = x
        ones = sum(s[l:r + 1])
        length = r - l + 1
        res += ones * (length - ones)
    return res

@timer
def run_solver(n):
    segs = generate_segments(n)
    s1 = [0 for _ in range(n)]
    s2 = [1 for _ in range(n)]
    for i in range(n):
        if i % 2 == 0:
            s1[i] = 1
            s2[i] = 0
    ans = s1 if calc(s1, segs) > calc(s2, segs) else s2
    # print(''.join(map(str, ans)))
    pass
    return ans

def main(n):
    return run_solver(n)

if __name__ == "__main__":
    main(10)