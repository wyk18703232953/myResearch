def main(n):
    # Deterministically generate input array s of length n
    # Example pattern: s[i] = i // 2  (creates duplicates and structure)
    s = [i // 2 for i in range(n)]

    s.sort()
    f = False
    z = s.count(0)
    p = 0
    for i in range(2, n):
        if s[i] == s[i - 1] and s[i - 1] == s[i - 2]:
            f = True
    for i in range(1, n):
        if s[i] == s[i - 1]:
            p += 1
            if i - 2 >= 0 and s[i - 2] == s[i - 1] - 1:
                f = True
    y = sum(s)
    t = n * (n - 1) // 2
    r = y - t
    if r % 2 == 0 or f or y == 0 or z >= 2 or p >= 2:
        # print("cslnb")
        pass

    else:
        # print("sjfnb")
        pass
if __name__ == "__main__":
    main(10)