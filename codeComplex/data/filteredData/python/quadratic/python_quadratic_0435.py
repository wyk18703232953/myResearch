def main(n):
    # Generate deterministic input based on n
    # Original input:
    # n: length of string
    # s2: string of digits of length n
    #
    # Here we interpret the new n as the length of the digit string.
    # Construct s2 as a deterministic pattern of '0'..'9'.
    s2 = ''.join(str((i % 10)) for i in range(n))

    # Original logic starts here (with generated inputs)
    s2 = list(s2)
    s = []
    for i in range(n):
        if s2[i] == '0':
            continue

        else:
            s.append(int(s2[i]))
    s1 = sum(s)
    n = len(s)
    l = []
    for i in range(2, n + 1):
        if s1 % i == 0:
            l.append(s1 // i)
    f = 0
    if len(s) == 0:
        f = 1
    for i in range(len(l)):
        c = 0
        if f == 1:
            break
        for j in range(n):
            c += s[j]
            if c == l[i]:
                c = 0
                if j == n - 1:
                    f = 1
            elif c < l[i]:
                c = c

            else:
                break
    if f == 0:
        # print('NO')
        pass

    else:
        # print('YES')
        pass
if __name__ == "__main__":
    main(10)