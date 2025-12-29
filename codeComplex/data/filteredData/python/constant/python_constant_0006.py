import math
import random

SPACE = ' '
ACCEL = 0.0  # will be set in get_time


def time(d=None, v=None, v0=0, steady=False):
    if steady:
        return d / v

    if d is None:
        # time to accelerate v0 to v
        return (v - v0) / ACCEL

    # time to go distance d while accelerating from v0
    if v is None:
        v = vel(d=d, v0=v0)
    return (2 * d) / (v + v0)


def dist(t=None, v=None, v0=0, steady=False):
    if steady:
        return v * t

    if t is None:
        # distance to accelerate v0 to v
        return (pow(v, 2) - pow(v0, 2)) / (2 * ACCEL)

    # distance to accelerate for time t
    return 0.5 * (v + v0) * t


def vel(d=None, t=None, v0=0, steady=False):
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
    ACCEL = a

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
        res = time(v=w) + time(
            v=vel(d=(d - dist(v=w)) / 2, v0=w),
            v0=w
        ) * 2

    # go from sign to end of the road
    x = d + dist(v=v) - dist(v=w)
    if x >= l:
        # reach end of the road before getting to top speed
        res += time(d=l - d, v0=w)
        return res
    return res + time(v=v, v0=w) + time(d=l - x, v=v, steady=True)


def main(n):
    """
    n: number of random test cases to generate.
    For each test case, generate (a, v, l, d, w) and print the time.
    """
    random.seed(0)
    for _ in range(n):
        # Generate reasonable random parameters
        a = random.randint(1, 10)          # acceleration
        v = random.randint(1, 100)         # max speed
        l = random.randint(1, 1000)        # total length
        d = random.randint(0, l)           # sign position within [0, l]
        w = random.randint(0, v)           # speed limit at sign

        t = get_time(a, v, l, d, w)
        print(a, v)
        print(l, d, w)
        print(t)


if __name__ == "__main__":
    main(5)