import collections
import bisect

def main(n):
    starting = [(i * 3) % (2 * n + 1) for i in range(n)]
    ending = [((i * 5) + 7) % (2 * n + 1) for i in range(n)]

    if not starting or not ending:
        # print(0)
        pass
        return

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
                loc_max = s[pos - 1] if pos - 1 >= 0 else maxim

        else:
            loc_max = maxim

        if ending[i] == minim:
            if end_count[minim] > 1:
                loc_min = minim

            else:
                pos = bisect.bisect_right(e, minim)
                if pos < len(e):
                    loc_min = e[pos]

                else:
                    loc_min = minim

        else:
            loc_min = minim

        ans = max(ans, loc_min - loc_max)

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)