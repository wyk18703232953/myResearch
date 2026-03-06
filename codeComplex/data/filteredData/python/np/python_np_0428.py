def main(n):
    # Map n to matrix dimensions and value range deterministically
    if n < 1:
        n = 1
    rows = n
    cols = max(1, n // 2)
    m = cols

    # Deterministically generate a 2D array "arrays" of size rows x cols
    # values are in [0, 10^9]
    MOD = 10**9 + 7
    arrays = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = (i * cols + j) * 1234567 % MOD
            row.append(val)
        arrays.append(row)

    full = (1 << m) - 1
    L = -1
    R = 10**9 + 1
    ans0 = 0
    ans1 = 0

    while L + 1 < R:
        check = (L + R) >> 1

        masks = {}
        for i, arr in enumerate(arrays):
            curr = 0
            for val in arr:
                curr <<= 1
                if val >= check:
                    curr |= 1
            masks[curr] = i

        isValid = False
        for k1 in masks:
            if isValid:
                break
            for k2 in masks:
                if k1 | k2 == full:
                    ans0 = masks[k1]
                    ans1 = masks[k2]
                    isValid = True
                    break

        if isValid:
            L = check
        else:
            R = check

    # Return 1-based indices to match original behavior
    return ans0 + 1, ans1 + 1


if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    result = main(10)
    print(result[0], result[1])