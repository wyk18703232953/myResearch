def main(n):
    # Generate deterministic parameters based on n
    # l <= r, moderate range compared to sums of A
    l = n
    r = 3 * n
    x = max(1, n // 4)

    # Deterministic array A of size n
    A = [i % 10 + (i // 3) for i in range(n)]

    count = 0
    # Iterate all non-empty subsets (same as original logic but with i>0)
    for i in range(1, 1 << n):
        total = 0
        mn = 10**9
        mx = -10**9
        for k in range(n):
            if i & (1 << k):
                val = A[k]
                total += val
                if val < mn:
                    mn = val
                if val > mx:
                    mx = val
        if l <= total <= r and mx - mn >= x:
            count += 1
    print(count)


if __name__ == "__main__":
    # Example call; adjust n for different scales
    main(10)