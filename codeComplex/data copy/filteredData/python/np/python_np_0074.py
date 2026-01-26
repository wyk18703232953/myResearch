def main(n):
    # Deterministic generation of a and b based on n
    # Interpret n as the maximum length of the strings
    # a is a pattern of '+' and '-' of length n
    # b is a pattern of '+', '-', and '?' of length n
    if n <= 0:
        return

    # Generate string a: alternating '+' and '-'
    a = "".join('+' if i % 2 == 0 else '-' for i in range(n))

    # Generate string b: periodic pattern '+', '-', '?'
    pattern = ['+', '-', '?']
    b = "".join(pattern[i % 3] for i in range(n))

    l = a.count("+") - a.count("-")
    k = b.count("?")
    if k == 0:
        if (b.count("+") - b.count("-")) == l:
            print(1)
        else:
            print(0)
    else:
        import math
        c = []
        t = 0
        r = k
        while r >= 0:
            c.append(r - t)
            t += 1
            r -= 1
        d = []
        for i in range(k + 1):
            d.append((math.factorial(k)) // (math.factorial(i) * math.factorial(k - i)))
        f = b.count("+") - b.count("-")
        if l - f in c:
            print((d[c.index(l - f)]) / sum(d))
        else:
            print(0)


if __name__ == "__main__":
    main(10)