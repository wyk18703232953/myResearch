def main(n):
    m = max(1, n // 3)
    a = [[(i * m + j) % (10**9 + 7) for j in range(m)] for i in range(n)]
    left = 0
    right = 10**9 + 1
    ans = (0, 0)
    while left < right:
        mid = (left + right) // 2
        masks = {}
        for i in range(n):
            mask = 0
            for j in a[i]:
                mask <<= 1
                if j >= mid:
                    mask += 1
            masks[mask] = i
        ok = False
        full_mask = (1 << m) - 1
        for m1 in masks:
            for m2 in masks:
                if m1 | m2 == full_mask:
                    ok = True
                    ans = (masks[m1] + 1, masks[m2] + 1)
                    break
            if ok:
                break
        if ok:
            left = mid + 1
        else:
            right = mid
    print(ans[0], ans[1])


if __name__ == "__main__":
    main(10)