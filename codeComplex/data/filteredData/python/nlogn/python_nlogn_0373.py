def main(n):
    import collections

    # Deterministic data generation
    # Map n to: number of elements = n, k = max(1, n//10)
    k = max(1, n // 10)

    # Generate an array with some repeated values and gaps
    # Values will be in a range roughly proportional to n
    # Example pattern: (i*2 + (i//3)) % (2*n+1)
    arr = [((i * 2) + (i // 3)) % (2 * n + 1) for i in range(n)]

    cs = collections.Counter(arr)
    ks = list(cs.keys())
    ks.sort()
    ans = 0
    for i in range(1, len(ks)):
        if ks[i] <= ks[i - 1] + k:
            continue

        else:
            ans += cs[ks[i - 1]]
    if ks:
        ans += cs[ks[-1]]
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)