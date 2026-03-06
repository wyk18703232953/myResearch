def main(n):
    from collections import defaultdict

    # Map n to matrix dimensions
    # Choose m as a small constant (original code uses 5)
    m = 5
    if n < 1:
        n_rows = 1
    else:
        n_rows = n

    # Deterministically generate arr of size n_rows x m
    # Use a simple arithmetic pattern
    arr = [[(i * m + j) % 100 for j in range(m)] for i in range(n_rows)]

    def check(num):
        bitmask = set()
        for i in range(n_rows):
            b = 0
            for j in range(m):
                if arr[i][j] >= num:
                    b ^= 1 << j
            bitmask.add(b)
        target = (1 << m) - 1
        for x in bitmask:
            for y in bitmask:
                if x | y == target:
                    return True
        return False

    # Binary search for ans
    start = 0
    end = 10 ** 9
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if check(mid):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

    # Reconstruct bitmasks to find indices
    bitmask = defaultdict(list)
    for i in range(n_rows):
        b = 0
        for j in range(m):
            if arr[i][j] >= ans:
                b += 1 << j
        bitmask[b].append(i + 1)

    target = (1 << m) - 1
    for x in bitmask:
        for y in bitmask:
            if x | y == target:
                # Output result to keep behavior
                print(bitmask[x][0], bitmask[y][0])
                return


if __name__ == "__main__":
    main(6)