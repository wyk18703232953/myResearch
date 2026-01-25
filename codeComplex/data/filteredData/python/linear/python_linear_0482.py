import sys
import math
import collections
import bisect

def main(n):
    if n <= 0:
        print(0)
        return

    # Deterministic construction of n intervals
    starting = [i for i in range(n)]
    ending = [i + (n // 2) + 1 for i in range(n)]

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

    print(ans)

if __name__ == "__main__":
    main(10)