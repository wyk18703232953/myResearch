import math

SPACE = ' '
ACCEL = 0.0


def time(d=None, v=None, v0=0, steady=False):
    if steady:
        return d / v
    if d is None:
        return (v - v0) / ACCEL
    if v is None:
        v = vel(d=d, v0=v0)
    return (2 * d) / (v + v0)


def dist(t=None, v=None, v0=0, steady=False):
    if steady:
        return v * t
    if t is None:
        return (pow(v, 2) - pow(v0, 2)) / (2 * ACCEL)
    return 0.5 * (v + v0) * t


def vel(d=None, t=None, v0=0, steady=False):
    if steady:
        return d / t
    if d is None:
        return t * ACCEL - v0
    return pow(2 * d * ACCEL + v0 ** 2, 0.5)


def can_ignore_sign(v, w, d):
    return v <= w or d <= dist(v=w)


def ignore_sign(v, w, l):
    dmax = dist(v=v)
    if l <= dmax:
        return time(d=l)
    return time(v=v) + time(d=l - dmax, v=v, steady=True)


def get_time(a, v, l, d, w):
    global ACCEL
    ACCEL = a

    if can_ignore_sign(v, w, d):
        return ignore_sign(v, w, l)

    tmax, dmax = time(v=v), dist(v=v)
    tlim_max, dlim_max = time(v=v, v0=w), dist(v=v, v0=w)
    if dmax + dlim_max <= d:
        res = tmax + time(d=d - dmax - dlim_max, v=v, steady=True) + tlim_max

    else:
        res = time(v=w) + time(v=vel(d=(d - dist(v=w)) / 2, v0=w), v0=w) * 2

    x = d + dist(v=v) - dist(v=w)
    if x >= l:
        res += time(d=l - d, v0=w)
        return res
    return res + time(v=v, v0=w) + time(d=l - x, v=v, steady=True)


def main(n):
    if n < 1:
        n = 1
    a = 1 + (n % 10)       # acceleration in [1,10]
    v = 10 + (n % 100)     # max speed in [10,109]
    l = max(1, n * 10)     # road length grows with n
    d = max(1, n * 5)      # distance to sign
    if d > l:
        d = l // 2 or 1
    w = 5 + (n % 50)       # speed limit in [5,54]
    result = get_time(a, v, l, d, w)
    # print(result)
    pass
if __name__ == "__main__":
    main(100)