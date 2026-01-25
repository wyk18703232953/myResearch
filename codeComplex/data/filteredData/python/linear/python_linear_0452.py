def main(n):
    # Interpret n as the length of strings s and t
    # Construct deterministic strings s and t based on n
    # s will contain a single '*' at a deterministic position (if n > 1)

    if n <= 0:
        return

    # Build s_chars and t_chars deterministically
    s_chars = []
    t_chars = []

    star_pos = 0 if n == 1 else (n // 2)  # position of '*' for s when n > 1

    for i in range(n):
        if i == star_pos and n > 1:
            s_chars.append('*')
        else:
            s_chars.append(chr(ord('a') + (i % 26)))

        # t is a simple shifted pattern to test mismatches/matches
        t_chars.append(chr(ord('a') + ((i + 1) % 26)))

    s = "".join(s_chars)
    t = "".join(t_chars)

    # Emulate original input structure (n, m, s, t)
    m = len(t)

    if n == 1:
        if s == t or s == '*':
            print('YES')
        else:
            print('NO')
    elif s.count('*') == 0:
        if s == t:
            print('YES')
        else:
            print('NO')
    elif n > m + 1:
        print('NO')
    else:
        l = s.split('*')
        x = t[:len(l[0])] if len(l[0]) > 0 else ""
        y = t[-len(l[1]):] if len(l[1]) > 0 else ""
        if (l[0] == x and l[1] == y) or (s[:1] == '*' and l[1] == y) or (l[0] == x and s[-1:] == '*'):
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(10)