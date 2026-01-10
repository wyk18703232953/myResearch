def main(n):
    from copy import deepcopy
    import itertools
    from bisect import bisect_left
    from bisect import bisect_right
    import math
    from collections import deque

    def generate_intervals(N):
        intervals = []
        for i in range(N):
            l = 2 * i
            r = 2 * i + 1
            intervals.append((l, r))
        return intervals

    N = n
    left = 0
    right = 1
    LIST = []
    intervals = generate_intervals(N)
    for l, r in intervals:
        LIST.append((l, left))
        LIST.append((r, right))

    LIST.sort()

    cnt = [0] * (N + 1)  # DO NOT USE cnt[0]

    if not LIST:
        print("")
        return

    n_curr = 1
    x = LIST[0][0]
    dir = left
    for item in LIST[1:]:
        if item[1] == left:
            if dir == left:
                cnt[n_curr] += item[0] - x
                n_curr += 1
                x = item[0]
                dir = left
            else:
                cnt[n_curr] += item[0] - x - 1
                n_curr += 1
                x = item[0]
                dir = left
        else:
            if dir == left:
                cnt[n_curr] += item[0] - x + 1
                n_curr -= 1
                x = item[0]
                dir = right
            else:
                cnt[n_curr] += item[0] - x
                n_curr -= 1
                x = item[0]
                dir = right

    print(" ".join(list(map(str, cnt[1:]))))


if __name__ == "__main__":
    main(5)