def sss(l, r, tt, a, m):
    f = -1
    while l <= r:
        mid = (l + r) >> 1
        if a[mid] - a[tt] <= m:
            f = mid
            l = mid + 1

        else:
            r = mid - 1
    return f

def core(a, m):
    f = 0
    l = len(a)
    Maxx = -1
    for i in range(0, l - 2):
        if a[i + 2] - a[i] <= m:
            k = sss(i + 2, l - 1, i, a, m)
            if k != -1:
                Maxx = max(Maxx, (a[k] - a[i + 1]) / (a[k] - a[i]))
    if Maxx == -1:
        return -1
    return Maxx

def main(n):
    if n < 3:
        a = [i for i in range(1, 4)]
        m = 1

    else:
        L = n
        a = [2 * i + (i // 3) for i in range(L)]
        if L >= 2:
            m = (a[L - 1] - a[0]) // 3 + 1

        else:
            m = 1
    res = core(a, m)
    if res == -1:
        # print(-1)
        pass

    else:
        # print("%.15f" % res)
        pass
if __name__ == "__main__":
    main(10)