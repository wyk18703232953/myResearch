def main(n):
    # Map n to problem parameters deterministically
    # Use n as number of elements, and derive l, r, x from n
    # Ensure n >= 1 to avoid empty range issues
    if n <= 0:
        print(0)
        return

    # Generate array a deterministically: a[i] = i+1
    a = [i + 1 for i in range(n)]

    # Define constraints deterministically based on n
    total_sum = n * (n + 1) // 2
    l = total_sum // 3
    r = total_sum * 2 // 3
    x = max(1, n // 3)

    cnt = 0

    for i in range(0, 1 << n):
        s = 0
        mn = int(1e18)
        mx = 0

        for j in range(0, n):
            if (i >> j) & 1:
                s += a[j]
                if a[j] < mn:
                    mn = a[j]
                if a[j] > mx:
                    mx = a[j]

        if s >= l and s <= r and (mx - mn) >= x:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main(10)