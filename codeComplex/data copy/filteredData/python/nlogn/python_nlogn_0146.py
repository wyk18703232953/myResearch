def main(n):
    # Interpret n as the length of the list a
    # Deterministically generate k and a
    k = max(2, n // 3 + 2)
    a = [(i * 2 + (i // 3)) for i in range(1, n + 1)]
    a.sort()
    s = set()
    for v in a:
        if (v % k != 0) or v // k not in s:
            s.add(v)
    # print(len(s))
    pass
if __name__ == "__main__":
    main(10)