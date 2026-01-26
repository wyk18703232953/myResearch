from math import sqrt


def dist(speed, time, a):
    # distance covered with initial speed 'speed' and constant acceleration 'a' in time 'time'
    return speed * time + a * time ** 2 / 2.0


def travelTime(distance, speed, a, v):
    # time to cover 'distance' starting with speed 'speed', max speed 'v', acceleration 'a'
    t_all = (-speed + sqrt(speed ** 2 + 2.0 * distance * a)) / a
    t_max = (v - speed) / a

    if t_max >= t_all:
        return t_all

    else:
        return t_max + (distance - dist(speed, t_max, a)) / v


def main(n):
    # 1) Generate test data from n (example scheme, can be adjusted):
    # Use n to scale total distance; keep acceleration and speeds reasonable.
    # a: acceleration, v: max speed, l: total distance, d: zone length, w: zone speed limit.
    a = 2.0 + (n % 4)        # acceleration in [2,5]
    v = 10.0 + (n % 20)      # max speed in [10,29]
    l = 100.0 + 5.0 * n      # total distance grows with n
    d = max(10.0, l * 0.3)   # first 30% of track is special zone (at least 10)
    d = min(d, l)            # cannot exceed total distance
    w = 5.0 + (n % 15)       # speed limit in [5,19]

    # 2) Core logic from original program
    if v <= w:
        ans = travelTime(l, 0.0, a, v)

    else:
        tw = w / a          # time to reach speed w from 0
        dw = dist(0.0, tw, a)

        if dw >= d:
            ans = travelTime(l, 0.0, a, v)

        else:
            # accelerate to w, then:
            # - symmetric accelerate/decelerate part within [0, d]
            # - then travel remaining l - d at speed up to v starting from w
            ans = tw + 2.0 * travelTime((d - dw) / 2.0, w, a, v) + travelTime(l - d, w, a, v)

    # print(ans)
    pass
if __name__ == "__main__":
    # example run with some n; in real use, caller should invoke main(n) directly
    main(10)