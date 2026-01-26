def main(n):
    # n is the size parameter: original problem required n divisible by 2
    # and the algorithm only works meaningfully when n % 4 != 2
    # For timing experiments we just run the algorithm for any n >= 2.
    # We construct a deterministic array a[1..n] such that
    # a[i] - a[i + n//2] is zero at some position if n is even and n % 4 != 2.
    # Here we simply choose a[i] = i and a[i + n//2] = i for i <= n//2 when possible.
    if n < 2:
        return

    # Precompute the values that would have been queried via `? i`
    # Using 1-based indexing logic from the original code
    a = [0] * (n + 1)  # index 0 unused

    if n % 2 == 0:
        half = n // 2
        # For i in [1, half], set a[i] = i and a[i + half] = i
        # This guarantees a[i] - a[i+half] == 0 for all i in [1, half]
        for i in range(1, half + 1):
            a[i] = i
            a[i + half] = i

    else:
        # For odd n, just fill deterministically (no special structure)
        for i in range(1, n + 1):
            a[i] = i

    got = [10**18] * (n + 5)

    def getnum(i):
        if got[i] == 10**18:
            # in the original interactive version, this would print a query
            # and read the answer; here we directly return from our array
            got[i] = a[i]
        return got[i]

    # Original main logic
    if n % 4 == 2:
        # the opposite person has a different parity
        # In the interactive problem this prints "! -1"
        # For timing experiments we just execute the same branch.
        _ = "-1"
        return

    else:
        lo = 1
        hi = n // 2 + 1
        t1 = getnum(lo)
        t2 = getnum(hi)
        lo2 = t1 - t2
        hi2 = t2 - t1
        if lo2 == 0:
            _ = "1"
            return

        else:
            while lo < hi:
                mid = (lo + hi) // 2
                mid2 = getnum(mid) - getnum(mid + n // 2)
                if mid2 == 0:
                    _ = str(mid)
                    break
                if (lo2 > 0) == (mid2 > 0):
                    lo = mid + 1

                else:
                    hi = mid - 1

            else:
                _ = str(lo)


if __name__ == "__main__":
    # Example deterministic call for timing experiments
    main(10)