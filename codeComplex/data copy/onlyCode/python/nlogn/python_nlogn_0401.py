from sys import stdin
from math import hypot


def main():
    l = stdin.read().splitlines()[1:]
    for i, s in enumerate(l):
        l[i] = [*map(float, s.split()), i]
    l.sort(key=lambda xyi: abs(xyi[0]))
    res = ['1'] * len(l)
    x, y, _ = l.pop()
    while(l):
        dx, dy, i=l.pop()
        a, b, u, v = x + dx, y + dy, x - dx, y - dy
        if hypot(a, b) < hypot(u, v):
            x, y = a, b
        else:
            x, y, res[i] = u, v, '-1'
    print(' '.join(res))


if __name__ == '__main__':
    main()
