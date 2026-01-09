def main(n):
    # n controls the length of x and y
    m = n

    # Deterministic generation of x and y
    # x: [0, 1, 2, ..., n-1]
    # y: [(i * 2) % n for i in range(n)]
    x = [i for i in range(n)]
    y = [(i * 2) % n for i in range(m)]

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
        # print(a)
        pass
if __name__ == "__main__":
    main(10)