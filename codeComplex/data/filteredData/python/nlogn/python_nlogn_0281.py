def main(n):
    d = {}
    # First set of pairs: use first n pairs
    # a from 0..n-1, b = i*2
    for i in range(n):
        a = i
        b = i * 2
        d[a] = b
    # Second set of pairs: also size n, to make scale clear
    # a from 0..n-1 (same keys), b = i*3 (may update)
    m = n
    for i in range(m):
        a = i
        b = i * 3
        if a in d and b > d[a]:
            d[a] = b
        elif a not in d:
            d[a] = b
    s = 0
    for i in d:
        s += d[i]
    # print(s)
    pass
if __name__ == "__main__":
    main(10)