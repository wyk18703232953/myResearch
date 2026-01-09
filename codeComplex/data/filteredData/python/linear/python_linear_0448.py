def main(n):
    # Interpret n as the common length of strings a and b (to keep logic meaningful)
    # Generate deterministic test data:
    # a will possibly contain one '*' at a deterministic position when n > 2
    # b will be a related string so that both YES/NO paths can be exercised for different n.
    m = n

    # Construct base string from lowercase letters deterministically
    base = ''.join(chr(ord('a') + (i % 26)) for i in range(n))

    if n == 0:
        a = ""
        b = ""
    elif n == 1:
        # simple case without '*'
        a = base
        b = base

    else:
        # place '*' at position p for a when n >= 2
        p = n // 2
        a = base[:p] + '*' + base[p+1:]

        # Construct b so that:
        # - For even n, b is designed to satisfy the matching condition
        # - For odd n, b is slightly modified to fail the matching
        if n % 2 == 0:
            # Matching case
            # We need to create b of length m = n such that:
            #   a[:i] == b[:i]
            #   t == tt where t = a[i+1:] and tt = b[m - n + 1 + i:] = b[i+1:]
            # So b should be identical to a but without the '*'
            b = base

        else:
            # Non-matching case, change one character in the tail
            b_list = list(base)
            # change last character deterministically
            b_list[-1] = chr(ord('z') - (n % 26))
            b = ''.join(b_list)

    # Original logic with a, b, n, m
    if '*' in a:
        c = a.replace('*', '')
        i = a.index('*')
        if c == b:
            # print("YES")
            pass
        elif a[:i] == b[:i]:
            t = a[i+1:]
            tt = b[m - n + 1 + i:]
            if t == tt and n - 1 <= m:
                # print("YES")
                pass

            else:
                # print("NO")
                pass

        else:
            # print("NO")
            pass
    elif n > m:
        # print("NO")
        pass

    else:
        if a == b:
            # print("YES")
            pass

        else:
            # print("NO")
            pass
if __name__ == "__main__":
    main(10)