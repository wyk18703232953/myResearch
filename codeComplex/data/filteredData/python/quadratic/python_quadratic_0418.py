def main(n):
    k = n
    # deterministically generate string s of length n using pattern of lowercase letters
    base = "abcdefghijklmnopqrstuvwxyz"
    s = "".join(base[i % 26] for i in range(n))

    i = -1
    for j in range(n - 1):
        if s[: j + 1] == s[n - j - 1 :]:
            i = j
    add = s[i + 1 :]
    for _ in range(k - 1):
        s += add
    # print(s)
    pass
if __name__ == "__main__":
    main(5)