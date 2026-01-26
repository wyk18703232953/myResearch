def main(n):
    # n controls the length of the string b
    m = max(1, n)

    # Deterministic construction of pattern a and text b:
    # - a contains exactly one '*'
    # - prefix and suffix lengths depend on n
    prefix_len = n // 3
    suffix_len = n // 4

    # Build prefix and suffix deterministically
    a1 = ''.join(chr(ord('a') + (i % 26)) for i in range(prefix_len))
    a2 = ''.join(chr(ord('z') - (i % 26)) for i in range(suffix_len))

    # Build b so that sometimes it matches and sometimes it doesn't,
    # deterministically depending on n (for scalability experiments)
    base = ''.join(chr(ord('a') + (i * 7 % 26)) for i in range(m))

    # If n is even, force a match; if odd, make it likely non-match
    if prefix_len + suffix_len <= m and n % 2 == 0:
        b = a1 + base[prefix_len:m - suffix_len] + a2

    else:
        b = base

    a = a1 + '*' + a2

    # Original algorithm logic starts here
    flag = 0
    for c in a:
        if c == '*':
            flag = 1
    if flag == 1:
        a1, a2 = a.split('*')
        Len1 = len(a1)
        Len2 = len(a2)
        b1 = b[:Len1]
        b2 = ''
        if Len2:
            b2 = b[-Len2:]
        if a1 == b1 and a2 == b2 and Len1 + Len2 <= len(b):
            # print('YES')
            pass

        else:
            # print('NO')
            pass

    else:
        if a == b:
            # print('YES')
            pass

        else:
            # print('NO')
            pass
if __name__ == "__main__":
    main(100)