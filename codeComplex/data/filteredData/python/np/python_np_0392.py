def main(n):
    # Interpret n as both number of rows and columns for scalability
    # n: size parameter, we set rows = n, cols = n (at least 1)
    if n <= 0:
        return
    rows = n
    cols = n

    # Deterministic generation of matrix a (rows x cols)
    # Values are constructed using a simple arithmetic formula
    a = [[(i * cols + j) % (10**9) for j in range(cols)] for i in range(rows)]

    mi = -1
    ma = 10**9
    ans = []

    while mi < ma:
        mid = (mi + ma + 1) // 2
        masks = {}
        for i in range(rows):
            currMask = 0
            for j in range(cols):
                if a[i][j] >= mid:
                    currMask |= 1 << j
            masks[currMask] = i
        req = (1 << cols) - 1
        possible = 0
        for mask_i in masks:
            if possible:
                break
            for mask_j in masks:
                if (mask_i | mask_j) == req:
                    possible = 1
                    ans = [masks[mask_i] + 1, masks[mask_j] + 1]
                    break
        if possible:
            mi = mid
        else:
            ma = mid - 1

    if ans:
        print(*ans)
    else:
        # If no pair found, still print something deterministic
        print(-1, -1)


if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(5)