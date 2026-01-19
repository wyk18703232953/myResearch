def main(n):
    # Interpret n as both number of arrays and their length
    # Ensure at least 1x1 to avoid degenerate behavior
    if n <= 0:
        n = 1

    num_arrays = n
    m = n

    # Deterministic data generation:
    # arrays[i][j] = (i * 131 + j * 17) % (n + 7)
    arrays = [
        [(i * 131 + j * 17) % (n + 7) for j in range(m)]
        for i in range(num_arrays)
    ]

    full = (1 << m) - 1
    L = -1
    R = 10 ** 9 + 1

    # Edge case: when m is large, bitmask (1 << m) can overflow practical limits.
    # To keep it scalable but still runnable for large n, cap m used for bitmask logic.
    # This does not change the control-flow structure, only limits problem size.
    # Here we cap at 20 bits for feasibility while preserving algorithm.
    if m > 20:
        m_eff = 20
        full = (1 << m_eff) - 1
        arrays_eff = [row[:m_eff] for row in arrays]
    else:
        m_eff = m
        arrays_eff = arrays

    while L + 1 < R:
        check = (L + R) >> 1

        masks = {}
        for i, arr in enumerate(arrays_eff):
            curr = 0
            for val in arr:
                curr <<= 1
                if val >= check:
                    curr |= 1
            masks[curr] = i

        isValid = False
        ans0 = ans1 = 0
        for k1 in masks:
            for k2 in masks:
                if (k1 | k2) == full:
                    ans0 = masks[k1]
                    ans1 = masks[k2]
                    isValid = True
                    break
            if isValid:
                break

        if isValid:
            L = check
        else:
            R = check

    # Return results instead of printing, to support benchmarking
    return ans0 + 1, ans1 + 1, L


if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    result = main(10)
    print(result)