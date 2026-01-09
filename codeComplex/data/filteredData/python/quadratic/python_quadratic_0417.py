def main(n):
    # Interpret n as the target length of initial string t
    tam = n if n > 0 else 1
    q = n if n > 0 else 1

    # Deterministically generate string t of length tam
    # Pattern: repeating lowercase letters 'a' to 'z'
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    t = "".join(alphabet[i % 26] for i in range(tam))

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