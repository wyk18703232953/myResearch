def main(n):
    # n 表示区间数量
    t = max(2, n)
    intervals = []
    for i in range(t):
        l = i
        r = i + 10
        intervals.append((l, r))

    l1 = l2 = -1
    r1 = r2 = 1 << 30
    il = ir = 0

    for i, (l, r) in enumerate(intervals):
        if l > l1:
            il, l1, l2 = i, l, l1
        elif l > l2:
            l2 = l
        if r < r1:
            ir, r1, r2 = i, r, r1
        elif r < r2:
            r2 = r

    ans = max(0, (r2 - l2, max(r1 - l2, r2 - l1))[il != ir])
    # print(ans)
    pass
if __name__ == "__main__":
    main(5)