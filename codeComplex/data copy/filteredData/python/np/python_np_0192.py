def main(n):
    # Scale parameters deterministically based on n
    l = n * 2
    r = n * 4
    x = max(1, n // 3)

    # Deterministically generate c of length n
    c = [i % 10 + i // 2 for i in range(n)]

    ans = 0

    for mask in range(2 ** n):
        cnt, csum = 0, 0
        mn, mx = 10 ** 18, -(10 ** 18)
        for i in range(n):
            if mask & (1 << i) != 0:
                cnt += 1
                csum += c[i]
                mn = min(mn, c[i])
                mx = max(mx, c[i])
        if (cnt >= 2) and (l <= csum <= r) and (mx - mn >= x):
            ans += 1

    print(ans)


if __name__ == "__main__":
    main(10)