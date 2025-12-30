import math
import random

SPACE = ' '
ACCEL = 0.0  # will be set inside get_time


def time(d=None, v=None, v0=0.0, steady=False):
    if steady:
        return d / v

    if d is None:
        # time to accelerate v0 to v
        return (v - v0) / ACCEL

    # time to go distance d while accelerating from v0
    if v is None:
        v = vel(d=d, v0=v0)
    return (2 * d) / (v + v0)


def dist(t=None, v=None, v0=0.0, steady=False):
    if steady:
        return v * t

    if t is None:
        # distance to accelerate v0 to v
        return (pow(v, 2) - pow(v0, 2)) / (2 * ACCEL)

    # distance to accelerate for time t
    return 0.5 * (v + v0) * t


def vel(d=None, t=None, v0=0.0, steady=False):
    if steady:
        return d / t

    if d is None:
        # velocity after accelerating from v0 for time t
        return t * ACCEL - v0

    # velocity after going distance d accelerating from v0
    return math.sqrt(2 * d * ACCEL + v0 ** 2)


def can_ignore_sign(v, w, d):
    return v <= w or d <= dist(v=w)


def ignore_sign(v, w, l):
    dmax = dist(v=v)
    if l <= dmax:
        return time(d=l)
    return time(v=v) + time(d=l - dmax, v=v, steady=True)


def get_time(a, v, l, d, w):
    global ACCEL
    ACCEL = float(a)

    v = float(v)
    l = float(l)
    d = float(d)
    w = float(w)

    if can_ignore_sign(v, w, d):
        return ignore_sign(v, w, l)

    # go to the sign
    tmax, dmax = time(v=v), dist(v=v)
    tlim_max, dlim_max = time(v=v, v0=w), dist(v=v, v0=w)
    if dmax + dlim_max <= d:
        #  0 <<< lim <<< max === sign <<< dlim_max
        #  0 <<<dlim === dmax=== sign <<< dlim_max
        res = tmax + time(d=d - dmax - dlim_max, v=v, steady=True) + tlim_max
    else:
        #  0 <<<dlim ... dmax=== sign <<< dlim_max
        res = time(v=w) + time(v=vel(d=(d - dist(v=w)) / 2, v0=w), v0=w) * 2

    # go from sign to end of the road
    x = d + dist(v=v) - dist(v=w)
    if x >= l:
        # reach end of the road before getting to top speed
        res += time(d=l - d, v0=w)
        return res
    return res + time(v=v, v0=w) + time(d=l - x, v=v, steady=True)


def generate_test_case(n):
    """
    根据规模 n 生成一组 (a, v, l, d, w) 测试数据。
    n 越大，数值范围越大。
    """
    # 基础上限随 n 增长
    base = max(10, n)
    max_a = max(1, base)
    max_v = max(5, base * 2)
    max_l = max(10, base * 10)
    max_d = max(5, base * 5)

    a = random.randint(1, max_a)
    v = random.randint(1, max_v)
    l = random.randint(1, max_l)
    d = random.randint(0, min(l, max_d))
    w = random.randint(0, v)

    return a, v, l, d, w


def main(n):
    """
    n: 规模参数，用于生成 n 组随机测试数据。
    返回值：长度为 n 的列表，每个元素为 (inputs, answer)，
    其中 inputs=(a, v, l, d, w)，answer 为对应的最短时间。
    """
    random.seed(0)  # 保证同一 n 下结果可复现
    results = []
    for _ in range(n):
        a, v, l, d, w = generate_test_case(n)
        t = get_time(a, v, l, d, w)
        results.append(((a, v, l, d, w), t))
    return results


if __name__ == '__main__':
    # 示例：生成并打印 3 组测试数据及结果
    for inputs, ans in main(3):
        a, v, l, d, w = inputs
        print(a, v)
        print(l, d, w)
        print(ans)