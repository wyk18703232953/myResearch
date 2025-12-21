def main(n):
    a = n
    b = str(a)
    c = []
    for i in range(2, a + 1):
        if a % i == 0:
            c.append(i)
    l = 0
    for j in c:
        r = str(j)
        t = len(r)
        o = 0
        for p in r:
            if p == "4" or p == "7":
                o = o + 1
        if o == t:
            l = l + 1
    if l > 0:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    print(main(28))