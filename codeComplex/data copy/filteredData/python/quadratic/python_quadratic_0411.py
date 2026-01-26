def main(n):
    # Interpret n as the initial string length tam
    # Set q = n as well, so total work scales with n
    tam = max(1, n)
    q = max(1, n)

    # Deterministically generate the initial string t of length tam
    # Pattern: repeated digits '0'..'9' based on index
    t = ''.join(str(i % 10) for i in range(tam))
    s = t

    posi = -1

    for j in range(tam - 1):
        if t[:j + 1] == t[tam - j - 1:]:
            posi = j

    add = t[posi + 1:]

    for _ in range(q - 1):
        s += add

    # print(s)
    pass
if __name__ == "__main__":
    main(10)