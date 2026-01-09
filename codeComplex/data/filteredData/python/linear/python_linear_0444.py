def main(n):
    # n controls the length of base pattern in s (excluding '*')
    # Construct deterministic n, m, s, t based on n
    
    # Ensure n is at least 1
    if n <= 0:
        n = 1

    # Pattern for s: first half 'a', then a '*', then second half 'b'
    # Total length of s is n
    # Place '*' at position mid (if possible)
    if n == 1:
        s = ['*']

    else:
        mid = n // 2
        s = []
        for i in range(n):
            if i == mid:
                s.append('*')
            elif i < mid:
                s.append('a')

            else:
                s.append('b')

    # Generate t so that sometimes it matches and sometimes not.
    # Let m be either n-1, n, or n+1 in a deterministic cycle.
    pattern_choice = n % 3
    if pattern_choice == 0:
        m = n - 1
    elif pattern_choice == 1:
        m = n

    else:
        m = n + 1
    if m < 0:
        m = 0

    # Now construct t (length m) deterministically from s
    # Case 1: try to make t a valid match when possible
    t = []
    if m >= max(0, n - 1):
        # We try to mimic the matching rule:
        # s_left + wildcard + s_right must fit inside t
        # For k = m - (n - 1) extra characters, place them in the middle
        # t = s_left + extra_chars + s_right
        idx = -1
        for i in range(len(s)):
            if s[i] == '*':
                idx = i
        if idx == -1:
            # No wildcard case: t is either equal or shifted
            for i in range(m):
                if i < n:
                    t.append(s[i])

                else:
                    # deterministic filler
                    t.append('z')

        else:
            s_left = s[0:idx]
            s_right = s[idx + 1:n]
            extra = m - (n - 1)
            # Build t = s_left + extra letters + s_right
            t.extend(s_left)
            # deterministic extra letters: alternating 'x' and 'y'
            for i in range(extra):
                t.append('x' if i % 2 == 0 else 'y')
            t.extend(s_right)

    else:
        # m < n-1, impossible to match per original logic, create any t of length m
        for i in range(m):
            # deterministic repeating pattern of characters
            c = chr(ord('a') + (i % 3))
            t.append(c)

    # Reuse original algorithm with generated n, m, s, t
    n_local = len(s)
    m_local = len(t)
    idx = -1
    for i in range(n_local):
        if s[i] == '*':
            idx = i
    if idx == -1:
        if s == t:
            # print('YES')
            pass

        else:
            # print('NO')
            pass

    else:
        if m_local < n_local - 1:
            # print('NO')
            pass

        else:
            s_left = s[0:idx]
            s_right = s[idx + 1:n_local]
            a = len(s_left)
            b = len(s_right)
            t_left = []
            t_right = []
            for i in range(a):
                t_left.append(t[i])
                t[i] = ''
            for i in range(b):
                t_right.append(t[m_local - i - 1])
            if s_left == t_left and s_right == t_right[::-1]:
                # print('YES')
                pass

            else:
                # print('NO')
                pass
if __name__ == "__main__":
    main(10)