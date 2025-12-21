def main(n):
    import random
    if n < 3:
        return -1
    m = random.randint(1, 10 * n)
    a = []
    cur = 0
    for _ in range(n):
        cur += random.randint(1, 10)
        a.append(cur)
    def sss(l, r, tt):
        f = -1
        while l <= r:
            mid = (l + r) >> 1
            if a[mid] - a[tt] <= m:
                f = mid
                l = mid + 1
            else:
                r = mid - 1
        return f
    Maxx = -1
    l = len(a)
    for i in range(0, l - 2):
        if a[i + 2] - a[i] <= m:
            k = sss(i + 2, l - 1, i)
            if k != -1:
                Maxx = max(Maxx, (a[k] - a[i + 1]) / (a[k] - a[i]))
    if Maxx == -1:
        return -1
    return float("%.15f" % Maxx)

if __name__ == "__main__":
    print(main(10))