from collections import defaultdict
import random

def main(n):
    s = []
    intervals = []
    for _ in range(n):
        l = random.randint(0, 10 * n)
        r = random.randint(l, l + 10)
        intervals.append((l, r))
        s += [(l, 0), (r, 1)]
    s.sort()
    now, rev = 0, defaultdict(int)
    for a, b in zip(s, s[1:]):
        now += 1 if a[1] == 0 else -1
        if a[1] == 0:
            rev[now] += b[0] - a[0] + (1 if b[1] == 1 else 0)
        elif b[0] != a[0]:
            rev[now] += b[0] - a[0] - (1 if b[1] == 0 else 0)
    res = []
    for i in range(1, n + 1):
        res.append(rev[i])
    return res

if __name__ == "__main__":
    print(*main(5))