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

def calc(s, segs):
    res = 0
    for x in segs:
        ones = sum(s[x[0]:x[1] + 1])
        res += ones * (x[1] - x[0] + 1 - ones)
    return res

@timer
def main(n: int):
    # 根据 n 生成测试数据
    # 生成区间数量 m，这里设为 n 的一半（至少为 1）
    m = max(1, n // 2)

    # 随机生成 m 个区间 [l, r]，0 <= l <= r < n
    segs = []
    for _ in range(m):
        l = random.randint(0, n - 1)
        r = random.randint(l, n - 1)
        segs.append([l, r])

    # 原逻辑
    s1 = [0 for _ in range(n)]
    s2 = [1 for _ in range(n)]
    for i in range(n):
        if i % 2 == 0:
            s1[i] = 1
            s2[i] = 0

    ans = s1 if calc(s1, segs) > calc(s2, segs) else s2
    print(''.join(map(str, ans)))
    return ans, segs

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)