def main(n):
    # Interpret n as the length of strings s and t
    # We deterministically construct:
    # - s: pattern string with exactly one '*'
    # - t: target string of the same length
    # Construction is fully deterministic and scales with n.
    if n < 2:
        # minimal meaningful size: n=2 (1 char + '*')
        n = 2

    # Place '*' at a deterministic position depending on n
    star_pos = n // 2

    # Build s: prefix of letters, then '*', then suffix of letters
    prefix = [chr(ord('a') + (i % 26)) for i in range(star_pos)]
    suffix = [chr(ord('a') + ((i + 7) % 26)) for i in range(n - star_pos - 1)]
    s = prefix + ['*'] + suffix

    # Build t so that it sometimes matches and sometimes not, deterministically
    # Rule: if n is even -> make t match; if n is odd -> differ at one position in prefix
    if n % 2 == 0:
        t = [chr(ord('a') + (i % 26)) for i in range(n)]

    else:
        t = [chr(ord('a') + (i % 26)) for i in range(n)]
        if star_pos > 0:
            # flip one character before star to break the match
            t[star_pos - 1] = chr(ord('z') - (t[star_pos - 1] != 'z'))

    m = n  # second integer in original input was the length of t

    # ----- Original core logic starts here -----
    s_list = s
    t_list = t

    if '*' not in s_list:
        if s_list == t_list:
            # print("YES")
            pass

        else:
            # print("NO")
            pass
        return

    i = s_list.index('*')
    if s_list[:i] == t_list[:i]:
        s_sub = s_list[i:]
        t_sub = t_list[i:]
        s_sub = s_sub[::-1]
        t_sub = t_sub[::-1]
        i = s_sub.index('*')

        if len(t_sub) >= i and s_sub[:i] == t_sub[:i]:
            # print("YES")
            pass

        else:
            # print("NO")
            pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to scale input size
    main(10)