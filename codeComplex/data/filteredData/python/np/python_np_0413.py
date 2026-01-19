def main(n):
    # Map n to matrix size: n = number of rows, m = min(n, 20) columns
    if n <= 0:
        return
    m = min(n, 20)

    # Deterministically generate arr based on n, i, j
    # Example: arr[i][j] = (i+1)* (j+2) + i + j
    arr = [[(i + 1) * (j + 2) + i + j for j in range(m)] for i in range(n)]

    # Precompute maximum value in arr for binary search upper bound
    max_val = max(max(row) for row in arr)

    def check(num):
        bitmask = set()
        for i in range(n):
            b = 0
            for j in range(m):
                if arr[i][j] >= num:
                    b ^= 1 << j
            bitmask.add(b)
        target = (1 << m) - 1
        for i_mask in bitmask:
            for j_mask in bitmask:
                if i_mask | j_mask == target:
                    return True
        return False

    start = 0
    end = max_val
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if check(mid):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

    from collections import defaultdict
    bitmask = defaultdict(list)
    for i in range(n):
        b = 0
        for j in range(m):
            if arr[i][j] >= ans:
                b += 1 << j
        bitmask[b].append(i + 1)
    target = (1 << m) - 1
    for i_mask in bitmask:
        for j_mask in bitmask:
            if i_mask | j_mask == target:
                print(bitmask[i_mask][0], bitmask[j_mask][0])
                return


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiment
    main(6)