def main(n):
    if n <= 0:
        return 0
    k = 2
    l = list(range(1, n + 1))
    d = dict()
    c = set()
    l.sort()
    for i in range(n):
        if not d.get(l[i]):
            c.add(l[i])
            d.setdefault(l[i] * k, 1)
    return len(c)


if __name__ == "__main__":
    print(main(10))