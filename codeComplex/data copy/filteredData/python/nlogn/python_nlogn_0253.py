def bin_ser(arr, curr):
    l = 0
    r = len(arr) - 1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] <= curr:
            ans = mid
            l = mid + 1

        else:
            r = mid - 1
    return ans


def main(n):
    # Deterministically construct input based on n
    # n is the size parameter: number of soldiers (n) and number of arrows (q)
    if n <= 0:
        return

    # Let q = n to keep sizes comparable and scalable
    q = n

    # arr: strengths of n soldiers, increasing sequence
    arr = [i + 1 for i in range(n)]

    # brr: q arrows, constructed deterministically with a pattern
    # to cover various behaviors (small, medium, large shots)
    su = sum(arr)
    brr = [(i * i) % (2 * su + 1) + 1 for i in range(1, q + 1)]

    # Original logic
    curr = 0
    for i in range(1, n):
        arr[i] = arr[i] + arr[i - 1]
    outputs = []
    for b in brr:
        curr += b
        pos = n - bin_ser(arr, curr) - 1
        if pos == 0:
            pos = n
        outputs.append(pos)
        if curr >= su:
            curr = 0

    # For timing experiments, we simply produce the outputs deterministically
    for v in outputs:
        # print(v)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)