def main(n):
    # Interpret n as the length of the list; choose a fixed deterministic k
    if n <= 0:
        print(0)
        return

    k = 2  # fixed deterministic multiplier

    # Deterministically generate list l of length n
    # Example pattern: l[i] = (i % 7) + 1, which produces small repeated values
    l = [(i % 7) + 1 for i in range(n)]

    d = dict()
    c = set()
    l.sort()
    for i in range(n):
        if not d.get(l[i]):
            c.add(l[i])
            d.setdefault(l[i] * k, 1)
    print(len(c))


if __name__ == "__main__":
    # Example deterministic call
    main(10)