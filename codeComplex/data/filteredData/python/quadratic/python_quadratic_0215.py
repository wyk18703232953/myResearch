def main(n):
    # Interpret n as the number of strings; let m scale with n deterministically
    if n <= 0:
        return
    m = max(1, n // 2)

    d = {x: 0 for x in range(m)}
    l = []

    # Deterministically generate n binary strings of length m
    # Bit at position x of string i is ((i + x) % 3 == 0)
    for i in range(n):
        s_chars = []
        for x in range(m):
            s_chars.append('1' if (i + x) % 3 == 0 else '0')
        s = ''.join(s_chars)
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