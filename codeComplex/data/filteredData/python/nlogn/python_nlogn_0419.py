from collections import defaultdict

def main(n):
    s = []
    for i in range(n):
        l = i * 2
        r = l + 2
        s.append((l, 0))
        s.append((r, 1))
    s.sort()
    now = 0
    rev = defaultdict(int)
    for a, b in zip(s, s[1:]):
        if a[1] == 0:
            now += 1
            rev[now] += b[0] - a[0]
            if b[1] == 1:
                rev[now] += 1
        else:
            now -= 1
            if b[0] != a[0]:
                rev[now] += b[0] - a[0]
                if b[1] == 0:
                    rev[now] -= 1
    for i in range(1, n + 1):
        print(rev[i], end=" ")

if __name__ == "__main__":
    main(10)