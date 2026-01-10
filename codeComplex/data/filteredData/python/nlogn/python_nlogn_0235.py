def main(n):
    if n <= 0:
        return

    # Deterministic generation of coordinates
    # X[i] = i, Y[i] = i^2 (mod some large number to keep values reasonable)
    X = [i for i in range(n)]
    Y = [(i * i) % (10**9 + 7) for i in range(n)]

    if n <= 3:
        print('YES')
        return

    # Deterministic replacement for random sampling:
    # For each iteration i, choose:
    #   a = i % n
    #   b = (i * 7 + 1) % n, and if a == b, b = (b + 1) % n
    for i in range(13):
        a = i % n
        b = (i * 7 + 1) % n
        if a == b:
            b = (b + 1) % n

        x0, y0 = X[a], Y[a]
        x1, y1 = X[b], Y[b]

        dx = x1 - x0
        dy = y1 - y0
        not_on_line = []
        for c in range(n):
            if c == a or c == b:
                continue
            x2, y2 = X[c], Y[c]
            Dx = x2 - x0
            Dy = y2 - y0
            if dx * Dy - dy * Dx != 0:
                not_on_line.append(c)
        if len(not_on_line) <= 1:
            print('YES')
            return

        if len(not_on_line) >= 2:
            a = not_on_line[0]
            b = not_on_line[1]
            x0, y0 = X[a], Y[a]
            x1, y1 = X[b], Y[b]

            dx = x1 - x0
            dy = y1 - y0
            can = True
            for c in not_on_line:
                if c == a or c == b:
                    continue
                x2, y2 = X[c], Y[c]
                Dx = x2 - x0
                Dy = y2 - y0
                if dx * Dy - dy * Dx != 0:
                    can = False
                    break
            if can:
                print('YES')
                return
    print('NO')


if __name__ == "__main__":
    main(10)