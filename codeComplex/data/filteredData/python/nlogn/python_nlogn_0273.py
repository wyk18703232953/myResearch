def solve(a):
    aa = sorted(a)
    maxr = aa[0]
    for ai in aa:
        if ai[2] != maxr[2]:
            if ai[1] <= maxr[1] and ai[0] >= maxr[0]:
                return (ai[2], maxr[2])
            if ai[1] >= maxr[1] and ai[0] <= maxr[0]:
                return (maxr[2], ai[2])
        if ai[1] > maxr[1]:
            maxr = ai
    return (-1, -1)

def main(n):
    a = []
    for i in range(n):
        l = i
        r = i + (i % 3) + 1
        a.append((l, r, i + 1))
    i, j = solve(a)
    print(i, j)

if __name__ == "__main__":
    main(10)