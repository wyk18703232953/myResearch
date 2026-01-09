def main(n):
    # Map n to (rows, columns)
    rows = n
    cols = max(1, n)

    m = cols
    d = {x: 0 for x in range(m)}
    l = []

    # Deterministically generate binary strings of length m
    # Pattern: s[i] = '1' if (row_index + i) % 3 == 0 else '0'
    for i in range(rows):
        s_list = ['1' if (i + x) % 3 == 0 else '0' for x in range(m)]
        s = ''.join(s_list)
        for x in range(m):
            if s[x] == '1':
                d[x] += 1
        l.append(s)

    for x in l:
        t = 0
        for y in range(m):
            if x[y] == '1':
                if d[y] == 1:
                    t = 1
                    break
        if t == 0:
            # print('YES')
            pass
            return
    # print('NO')
    pass
if __name__ == "__main__":
    main(10)