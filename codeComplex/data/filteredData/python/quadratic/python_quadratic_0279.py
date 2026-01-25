def main(n):
    # n controls the length of the sequences x and y
    # ensure n is at least 1 to avoid trivial empty behavior
    if n <= 0:
        return

    # deterministically generate x and y based on n
    # x: [0, 1, 2, ..., n-1]
    # y: [1, 2, 3, ..., n]
    x = [i for i in range(n)]
    y = [i + 1 for i in range(n)]

    out = []
    first = 11
    for a in range(len(x)):
        for b in range(len(y)):
            if y[b] == x[a]:
                if first < a:
                    first = a
                    out.append(y[b])
                    b += 1
                else:
                    out.insert(0, y[b])
                    b += 1
            else:
                b += 1
    out.reverse()
    for a in out:
        print(a)


if __name__ == "__main__":
    # example call; you can change n to test different scales
    main(10)