def main(n):
    # Ensure n is non-negative
    if n < 0:
        n = 0

    # Deterministically generate s and t based on n
    # s: repeating 'a'..'z'
    # t: shifted pattern so that t[i] != s[i] often, to exercise the logic
    s_chars = [chr(97 + (i % 26)) for i in range(n)]
    t_chars = [chr(97 + ((i + 1) % 26)) for i in range(n)]
    s = "".join(s_chars)
    t = "".join(t_chars)

    p = [-1, -1]  # kept to preserve original structure, though unused
    a = [[-1] * 26 for _ in range(26)]
    k = 0

    for i in range(n):
        if t[i] != s[i]:
            k += 1

    for i in range(n):
        if t[i] != s[i]:
            ti = ord(t[i]) - 97
            si = ord(s[i]) - 97
            if a[ti][si] != -1:
                print(k - 2)
                print(a[ti][si] + 1, i + 1)
                return
            a[si][ti] = i

    for i in range(n):
        if t[i] != s[i]:
            si = ord(s[i]) - 97
            for j in range(26):
                if a[j][si] != -1:
                    print(k - 1)
                    print(a[j][si] + 1, i + 1)
                    return
            a[si][ord(t[i]) - 97] = i

    print(k)
    print(-1, -1)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)