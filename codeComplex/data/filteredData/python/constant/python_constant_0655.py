def main(n):
    # Deterministically generate 3 points based on n
    # Interpret n as a scale for coordinate magnitude
    # Points: (n, n), (2n, n//2), (3n, (3n)//2)
    a = [
        (n, n),
        (2 * n, n // 2),
        (3 * n, (3 * n) // 2),
    ]

    a.sort()

    up1 = a[1][1] >= a[0][1]
    up2 = a[2][1] >= a[0][1]
    ans = {a[0]}
    x, y = a[0]
    if up1 and up2:
        while y < min(a[1][1], a[2][1]):
            y += 1
            ans.add((x, y))
        while x < a[2][0]:
            x += 1
            ans.add((x, y))
        hx, hy = a[2] if a[2][1] > a[1][1] else a[1]
        while hy > y:
            ans.add((hx, hy))
            hy -= 1

    else:
        dn1 = a[1][1] <= a[0][1]
        dn2 = a[2][1] <= a[0][1]
        ans = {a[0]}
        x, y = a[0]
        if dn1 and dn2:
            while y > max(a[1][1], a[2][1]):
                y -= 1
                ans.add((x, y))
            while x < a[2][0]:
                x += 1
                ans.add((x, y))
            lx, ly = a[2] if a[2][1] < a[1][1] else a[1]
            while ly < y:
                ans.add((lx, ly))
                ly += 1

        else:
            x, y = a[0]
            ans = {a[0]}
            while x < a[2][0]:
                x += 1
                ans.add((x, y))
            dy = 1 if a[1][1] <= a[0][1] else -1
            xx, yy = a[1]
            while yy != a[0][1]:
                ans.add((xx, yy))
                yy += dy
            dy = 1 if a[2][1] <= a[0][1] else -1
            xx, yy = a[2]
            while yy != a[0][1]:
                ans.add((xx, yy))
                yy += dy

    ans = sorted(ans)
    # print(len(ans))
    pass
    # print('\n'.join('%d %d' % (x, y) for x, y in ans))
    pass
if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(10)