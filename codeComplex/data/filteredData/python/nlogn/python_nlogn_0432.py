def main(n):
    import math

    # Deterministically generate input array s of length n
    # Example pattern: s[i] = (i * 3) % (n + 7)
    s = [(i * 3) % (n + 7) for i in range(n)]

    d = dict()
    for i in range(n):
        d[s[i]] = d.get(s[i], 0) + 1

    rem = 0
    for i in range(n):
        ok = False
        for j in range(31):
            x = 2 ** j - s[i]
            c = d.get(x, 0)
            if c > 1 or (c == 1 and s[i] != x):
                ok = True
                break
        if ok is False:
            rem += 1

    # print(rem)
    pass
if __name__ == "__main__":
    main(10)