def main(n):
    # Deterministically generate n, m, a, b
    # Interpret n as the base length for strings a and b
    # Ensure m >= n to respect the original first line "n m"
    m = n + (n // 2)

    # Construct pattern string a of length n with exactly one '*'
    # Position of '*' is deterministically chosen as n // 2
    if n == 0:
        a = "*"
        m = 1

    else:
        star_pos = n // 2
        prefix = "".join(chr(ord('a') + (i % 3)) for i in range(star_pos))
        suffix = "".join(chr(ord('x') - (i % 3)) for i in range(n - star_pos - 1))
        a = prefix + "*" + suffix

    # Construct b based on m to control match/no-match behavior deterministically
    # Let b start with the same prefix as a's prefix, end with same suffix,
    # and fill the middle with a deterministic pattern.
    a_parts = a.split('*')
    a1 = a_parts[0]
    a2 = a_parts[1] if len(a_parts) > 1 else ""

    middle_len = max(0, m - len(a1) - len(a2))
    middle = "".join(chr(ord('k') + (i % 5)) for i in range(middle_len))
    b = a1 + middle + a2

    # Original core logic
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
    main(10)