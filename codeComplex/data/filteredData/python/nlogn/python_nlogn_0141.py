def main(n):
    # Interpret n as the length of the list l
    k = 3  # fixed deterministic value
    # Deterministically generate list l based on n
    l = [(i * 2 + (i // 3)) for i in range(1, n + 1)]
    l = sorted(l)

    res = set()
    for i in l:
        if i // k not in res or i % k != 0:
            res.add(i)

    print(len(res))


if __name__ == "__main__":
    main(10)