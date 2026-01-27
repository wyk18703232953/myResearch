def main(n):
    # n controls the length of the two strings
    l = max(2, n)
    # Deterministically generate two binary strings of length l
    s0 = [('0' if (i % 3) != 0 else '1') for i in range(l)]
    s1 = [('0' if (i % 2) == 0 else '1') for i in range(l)]
    s = [s0, s1]

    ans = 0
    i = 0
    while i < l - 1:
        a = (s[0][i], s[0][i + 1], s[1][i], s[1][i + 1])
        if a.count("0") == 4:
            ans += 1
            s[0][i + 1] = "X"
            i += 1
        elif a.count("0") == 3:
            ans += 1
            i += 2

        else:
            i += 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)