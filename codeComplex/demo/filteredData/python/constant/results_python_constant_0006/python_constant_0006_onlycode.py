'''
Jana Goodman

5d follow traffic rules

accel formulas:
    t = (v1 - v0) / a
    d = (v1 - v0)t / 2
    v = sqr (2ad)

no accel: d = vt -- t = d / v -- v = d / t

'''
import math

SPACE = ' '


def get_data(file_name):
    result = list()
    state = 0
    data = list()
    # [a, v, l, d, w, answer]
    try:
        for line in open(file_name, 'r').readlines():
            line = line.strip()
            if state == 0:
                if line == 'Input':
                    data = list()
                    state = 1
                elif line == 'Answer':
                    state = 2
            elif state == 1:
                data += list(map(int, line.split(SPACE)))
                state = 11
            elif state == 11:
                data += list(map(int, line.split(SPACE)))
                state = 0
            elif state == 2:
                data.append(float(line))
                result.append(data)
                state = 0
    except FileNotFoundError:
        print(f'File {file_name} not found.')
    return result


# no accel: d = vt -- t = d / v -- v = d / t

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
    return (1 / 2) * (v + v0) * t


def vel(d=None, t=None, v0=0, steady=False):
    if steady:
        return d / t

    if d is None:
        # velocity after accelerating from v0 for time t
        return t * ACCEL - v0

    # velocity after going distance d accelerating from v0
    return pow(2 * d * ACCEL + v0 ** 2, 1 / 2)

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
        res = time(v=w) + time(v=vel(d=(d - dist(v=w)) / 2, v0=w), v0=w) * 2

    # go from sign to end of the road
    x = d + dist(v=v) - dist(v=w)
    if x >= l:
        # reach end of the road before getting to top speed
        res += time(d=l - d, v0=w)
        return res
    return res + time(v=v, v0=w) + time(d=l - x, v=v, steady=True)


if __name__ == '__main__':
    a, v = map(int, input().split())
    l, d, w = map(int, input().split())
    print(get_time(a, v, l, d, w))

# --------- testing
    # cases = get_data('testdata.txt')
    # for i, [a, v, l, d, w, ans] in enumerate(cases, 1):
    #     if a == 6 and v == 80:
    #         debug = 1
    #     my_ans = get_time(a, v, l, d, w)
    #     if abs(my_ans - ans) >= pow(10, -6):
    #         print(f'Case {i} My answer: {my_ans} -- Right answer: {ans}')
    #     else:
    #         print(f'Case {i} OK')
