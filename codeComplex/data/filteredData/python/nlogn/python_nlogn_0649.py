from bisect import bisect_left

def main(n):
    MAX = 10**9
    if n <= 0:
        n = 1
    m = 2 * n

    v = [(i * 3 + 1) % MAX for i in range(n)]
    v.sort()

    h = []
    for j in range(m):
        x1 = 1 if j % 2 == 0 else 2
        x2 = (j * 5 + 7) % MAX
        if x1 == 1:
            h.append(x2)
    h.sort()

    lh = len(h)
    if lh == 0:
        print(0)
    elif n == 0:
        print(lh - bisect_left(h, MAX))
    else:
        mn = n + lh - bisect_left(h, MAX)
        for i in range(n):
            mn = min(mn, lh - bisect_left(h, v[i]) + i)
        print(mn)


if __name__ == "__main__":
    main(10)