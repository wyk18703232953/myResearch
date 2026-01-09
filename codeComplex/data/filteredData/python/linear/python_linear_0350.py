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

def calc(s, segs):
    res = 0
    for x in segs:
        ones = sum(s[x[0]:x[1] + 1])
        res += ones * (x[1] - x[0] + 1 - ones)
    return res

@timer
def main(n):
    if n <= 0:
        return ""
    m = max(1, n // 2)
    segs = []
    for i in range(m):
        l = i % n
        r = (l + (i * 3) % n)
        if l > r:
            l, r = r, l
        segs.append([l, r])
    s1 = [0 for _ in range(n)]
    s2 = [1 for _ in range(n)]
    for i in range(n):
        if i % 2 == 0:
            s1[i] = 1
            s2[i] = 0
    ans = s1 if calc(s1, segs) > calc(s2, segs) else s2
    result = ''.join(map(str, ans))
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(1000)