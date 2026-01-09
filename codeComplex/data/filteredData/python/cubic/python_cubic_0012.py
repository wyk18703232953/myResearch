def main(n):
    # Deterministically generate input string s of length n
    # Pattern: repeating 'abc' to form a string of length n
    base = 'abc'
    repeats = n // len(base) + 1
    s = (base * repeats)[:n]

    o = len(s)
    k = 0
    for i in range(o):
        r = {0}
        for j in range(o - i + 1):
            if s[j:j + i] in r:
                k = max(i, k)

            else:
                r.add(s[j:j + i])
    # print(k)
    pass
if __name__ == "__main__":
    main(1000)