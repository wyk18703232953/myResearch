import collections
import bisect

def main(n):
    # Deterministically generate n intervals [starting[i], ending[i]]
    # starting[i] and ending[i] are constructed so that starting[i] <= ending[i]
    starting = []
    ending = []
    for i in range(n):
        x = i
        y = i + (i % 5)
        if x > y:
            x, y = y, x
        starting.append(x)
        ending.append(y)

    ans = 0
    start_count = collections.Counter(starting)
    end_count = collections.Counter(ending)
    s = starting.copy()
    s.sort()
    e = ending.copy()
    e.sort()
    maxim = max(starting)
    minim = min(ending)

    for i in range(n):
        if starting[i] == maxim:
            if start_count[maxim] > 1:
                loc_max = maxim

            else:
                pos = bisect.bisect_left(s, maxim)
                loc_max = s[pos - 1]

        else:
            loc_max = maxim

        if ending[i] == minim:
            if end_count[minim] > 1:
                loc_min = minim

            else:
                pos = bisect.bisect_right(e, minim)
                loc_min = e[pos]

        else:
            loc_min = minim

        ans = max(ans, loc_min - loc_max)

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)