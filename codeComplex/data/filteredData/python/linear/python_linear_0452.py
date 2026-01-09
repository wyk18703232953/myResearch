def main(n):
    # n controls the length of s and t
    # Ensure minimum size to avoid degenerate negative indices
    if n < 1:
        n = 1
    m = n

    # Deterministically construct s with a single '*' near the middle
    # Pattern: increasing letters with one '*' inserted
    base_chars = [chr(ord('a') + (i % 26)) for i in range(n)]
    star_pos = n // 2
    if n == 1:
        # For n = 1, choose either '*' or a single character deterministically
        if n % 2 == 0:
            s = '*'

        else:
            s = base_chars[0]

    else:
        s_list = base_chars[:]
        s_list[star_pos] = '*'
        s = ''.join(s_list)

    # Deterministically construct t related to s
    # Make t same length m, with a small modification based on n
    t_chars = []
    for i in range(m):
        if i == (n // 3):
            # introduce a deterministic difference at one position
            t_chars.append(chr(ord('z') - (i % 26)))

        else:
            if base_chars:
                t_chars.append(base_chars[i % len(base_chars)])

            else:
                t_chars.append('a')
    t = ''.join(t_chars)

    # Original logic, now using generated n, m, s, t
    if n == 1:
        if s == t or s == '*':
            # print('YES')
            pass

        else:
            # print('NO')
            pass
    elif s.count('*') == 0:
        if s == t:
            # print('YES')
            pass

        else:
            # print('NO')
            pass
    elif n > m + 1:
        # print('NO')
        pass

    else:
        l = s.split('*')
        x = t[:len(l[0])]
        y = t[-len(l[1]):] if len(l[1]) > 0 else ''
        if (l[0] == x and l[1] == y) or (s[:1] == '*' and l[1] == y) or (l[0] == x and s[-1:] == '*'):
            # print('YES')
            pass

        else:
            # print('NO')
            pass
if __name__ == "__main__":
    main(10)