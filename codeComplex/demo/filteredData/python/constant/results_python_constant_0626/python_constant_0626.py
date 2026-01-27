import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools

inf = 10**20
eps = 1.0 / 10**13
mod = 10**9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def main(n):
    aa = []
    for i in range(n):
        a = i
        b = 2 * n + i
        aa.append((a, b))

    r = []
    for a, b in aa:
        al = a + (1 - a % 2)
        ar = b - (1 - b % 2)
        sa = (ar - al) // 2 + 1
        tr = -(al + ar) * sa // 2

        bl = a + (a % 2)
        br = b - (b % 2)
        sb = (br - bl) // 2 + 1
        tr += (bl + br) * sb // 2
        r.append(tr)

    return "\n".join(map(str, r))


if __name__ == "__main__":
    # print(main(10))
    pass