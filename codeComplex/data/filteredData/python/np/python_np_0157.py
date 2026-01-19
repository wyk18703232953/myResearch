def main(n):
    # Map n to original parameters deterministically
    # Ensure at least 1 element
    n = max(1, int(n))

    # Deterministic construction of l, r, x based on n
    # l is about n, r is about 3n, x is about n//3
    l = n
    r = 3 * n
    x = max(1, n // 3)

    # Deterministic diff list of length n
    # Example pattern: i + 1 for 0 <= i < n
    diff = [i + 1 for i in range(n)]

    ans = 0

    # We need to iterate over all subsets; use a for-loop over bitmasks
    # Note: for large n this is exponential and will be slow, but preserves logic
    for mask in range(1 << n):
        currSum = 0
        maxim = 0
        minim = 1000001
        ptr = n - 1
        m = mask

        # Use m as a working copy so mask isn't destroyed (not strictly needed here,
        # but preserves the original algorithmic structure where i was mutated)
        while m > 0:
            if m & 1:
                v = diff[ptr]
                currSum += v
                if v > maxim:
                    maxim = v
                if v < minim:
                    minim = v
            ptr -= 1
            m >>= 1

        if l <= currSum <= r:
            if maxim - minim >= x and minim != 1000001:
                ans += 1

    print(ans)


if __name__ == "__main__":
    # Example deterministic call for timing experiments
    main(10)