def main(n):
    # Interpret n as the common length of strings s and t, and set m = n
    m = n

    # Deterministic construction of s and t:
    # - Prefix: first n//3 characters identical
    # - Middle: place one '*' in s, corresponding character in t is 'a'
    # - Suffix: alternate characters to sometimes match, sometimes not
    # Ensure at least length 1
    if n <= 0:
        n = 1
        m = 1

    # Build s and t as lists of characters
    s_list = []
    t_list = []

    # prefix length
    prefix_len = n // 3
    if prefix_len > 0:
        for i in range(prefix_len):
            ch = chr(ord('a') + (i % 3))  # 'a','b','c' cycle
            s_list.append(ch)
            t_list.append(ch)

    # position for '*' in s (if possible)
    if n > 1:
        star_pos = min(prefix_len, n - 1)

    else:
        star_pos = 0

    for i in range(prefix_len, n):
        if i == star_pos:
            s_list.append('*')
            t_list.append('a')

        else:
            # deterministic but varying pattern
            s_list.append(chr(ord('d') + (i % 3)))  # 'd','e','f' cycle
            t_list.append(chr(ord('d') + ((i + 1) % 3)))  # shifted

    s = "".join(s_list)
    t = "".join(t_list)

    # Original core logic
    if n - 1 > m:
        # print('NO')
        pass

    else:
        try:
            a = s.index('*')
        except:
            a = -1
        if a == -1:
            if s == t:
                # print('YES')
                pass

            else:
                # print('NO')
                pass

        else:
            for i in range(a):
                if s[i] != t[i]:
                    # print('NO')
                    pass
                    return
            i = 1
            while m - i >= a and n - i > a:
                if s[n - i] != t[m - i]:
                    # print('NO')
                    pass
                    return
                i += 1
            # print('YES')
            pass
if __name__ == "__main__":
    # Example deterministic call for testing / benchmarking
    main(10)