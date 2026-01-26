def main(n):
    if n < 2:
        n = 2
    n_val = n
    m_val = n
    size = n_val + m_val
    xs = [i for i in range(size)]
    ts = [1 if i % (n_val + 1) == 0 else 0 for i in range(size)]
    pos = [-1 for _ in range(size)]
    if ts[0]:
        pos[0] = 0
    for i in range(1, size):
        pos[i] = pos[i - 1]
        if ts[i]:
            pos[i] += 1
    result = [0 for _ in range(m_val)]
    left = 0
    right = 0
    for i in range(size):
        if ts[i] == 0:
            right = max(i, right)
            while right + 1 < size and not ts[right]:
                right += 1
            mP, mD = 0, 20000000
            if ts[left]:
                mP = pos[left]
                mD = xs[i] - xs[left]
            if ts[right] and xs[right] - xs[i] < mD:
                mD = xs[right] - xs[i]
                mP = pos[right]
            if 0 <= mP < m_val:
                result[mP] += 1

        else:
            left = i
    # print(*result)
    pass
if __name__ == "__main__":
    main(10)