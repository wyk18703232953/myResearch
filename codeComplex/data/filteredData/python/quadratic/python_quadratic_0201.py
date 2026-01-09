def main(n):
    m = n
    a = []
    for i in range(n):
        val = 0
        for j in range(m):
            if (i + j) % 3 == 0:
                val |= 1 << j
        a.append(val)

    s = 0
    t = 0
    for x in a:
        t |= s & x
        s |= x
    # print(('YES', 'NO')[all(x & s & ~t for x in a)])
    pass
if __name__ == "__main__":
    main(10)