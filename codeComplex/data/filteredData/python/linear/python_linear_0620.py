def main(n):
    # Interpret n as the number of "shops" (m); let number of "positions" be 2*m
    # So original: n_original + m_original = 2*m  and m_original = m
    # => n_original = m
    m = max(1, n)
    total = 2 * m  # corresponds to n + m in original code

    # Deterministic generation of xs (positions), strictly increasing
    # For example: xs[i] = i
    xs = list(range(total))

    # Deterministic generation of ts:
    # First m positions are type-1 (ts[i]=1), next m positions are type-0 (ts[i]=0)
    # This guarantees both kinds appear and matches original constraints (need some 1s and 0s)
    ts = [1 if i < m else 0 for i in range(total)]

    # Core logic from original program, unchanged
    pos = [-1 for _ in range(total)]
    if ts[0]:
        pos[0] = 0
    for i in range(1, total):
        pos[i] = pos[i - 1]
        if ts[i]:
            pos[i] += 1

    result = [0 for _ in range(m)]
    left = 0
    leftC = 0
    right = 0
    rightC = 0

    for i in range(total):
        if ts[i] == 0:
            right = max(i, right)
            while right + 1 < total and not ts[right]:
                right += 1
            mP, mD = 0, 20000000
            if ts[left]:
                mP = pos[left]
                mD = xs[i] - xs[left]
            if ts[right] and xs[right] - xs[i] < mD:
                mD = xs[right] - xs[i]
                mP = pos[right]
            result[mP] += 1

        else:
            left = i

    # print(*result)
    pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10)