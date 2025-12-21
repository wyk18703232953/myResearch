def main(n, k=7):
    a = [i + 1 for i in range(n)]
    b = []
    for i in range(11):
        c = {}
        p10 = 10 ** i
        for j in range(n):
            d = (a[j] * p10) % k
            if d in c:
                c[d] += 1
            else:
                c[d] = 1
        b.append(c)
    s = 0
    for i in range(n):
        ai = a[i]
        cmod = ai % k
        d = (k - cmod) % k
        l = len(str(ai))
        if d in b[l]:
            s += b[l][d]
        if (ai * (10 ** l)) % k == d:
            s -= 1
    return s

if __name__ == "__main__":
    print(main(10))