def getminmax(n, m, a):
    l = 0
    h = 1000000009

    while l < h:
        mid = (l + h + 1) // 2
        exists = existsequalorbig(mid, m, a)
        if exists:
            l = mid
        else:
            h = mid - 1
    return l


def existsequalorbig(mid, m, a):
    global idx1
    global idx2
    global VALD

    abw = []
    hs = set()

    for i in range(len(a)):
        v = 0
        for j in range(m):
            if a[i][j] >= mid:
                v |= 1
            v <<= 1
        v >>= 1
        if v not in hs:
            hs.add(v)
            abw.append([i, v])

    for i in range(len(abw)):
        for j in range(i, len(abw)):
            if abw[i][1] | abw[j][1] == VALD:
                idx1 = abw[i][0]
                idx2 = abw[j][0]
                return True

    return False


def main(n):
    global idx1
    global idx2
    global VALD

    m = 5
    idx1 = 0
    idx2 = 0
    VALD = int(pow(2, m) - 1)

    a = []
    for i in range(n):
        row = [((i + 1) * (j + 2)) % 100 for j in range(m)]
        a.append(row)

    getminmax(n, m, a)

    print(str(idx1 + 1) + ' ' + str(idx2 + 1))


if __name__ == "__main__":
    main(1000)