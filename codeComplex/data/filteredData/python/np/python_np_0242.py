def main(n):
    # Map n to problem parameters deterministically
    # n: number of elements
    if n <= 0:
        print(0)
        return

    # Define l, r, x based on n in a deterministic scalable way
    # Sum is between l and r, and max-min >= x
    l = n * (n + 1) // 4  # roughly quarter of sum of 1..n
    r = n * (n + 1) // 2  # full sum of 1..n
    x = max(1, n // 4)

    # Deterministic array a of size n
    a = [i + 1 for i in range(n)]

    cnt = 0

    for i in range(0, 1 << n):
        total = 0
        mn = int(1e18)
        mx = 0

        for j in range(0, n):
            if (i >> j) & 1:
                val = a[j]
                total += val
                if val < mn:
                    mn = val
                if val > mx:
                    mx = val

        if total >= l and total <= r and (mx - mn) >= x:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main(10)