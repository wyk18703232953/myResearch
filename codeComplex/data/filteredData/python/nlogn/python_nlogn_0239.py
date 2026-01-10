def main(n):
    # n is the number of points
    if n <= 0:
        return

    # Deterministic point generation:
    # For time-complexity experiments we'll generate points in a structured way.
    # Example pattern:
    # First ~n//3 points on line y = x
    # Next ~n//3 points on line y = 2x + 1
    # Remaining points off those lines: y = (i % 5) * x + (i // 5)
    points = []
    for i in range(n):
        if i < n // 3:
            x = i
            y = i
        elif i < 2 * n // 3:
            x = i
            y = 2 * i + 1
        else:
            x = i
            y = (i % 5) * i + (i // 5)
        points.append([x, y])

    if n < 5:
        print('YES')
        return

    st = [False] * n

    def run(first, second):
        dx = first[0] - second[0]
        dy = first[1] - second[1]

        for idx, p in enumerate(points):
            if st[idx]:
                continue
            if dx == 0:
                if p[0] == first[0]:
                    st[idx] = True
            elif dy == 0:
                if p[1] == first[1]:
                    st[idx] = True
            else:
                if (p[0] - first[0]) * dy == (p[1] - first[1]) * dx:
                    st[idx] = True

    def check(fi, si):
        for i in range(n):
            st[i] = (i == fi or i == si)

        run(points[fi], points[si])

        fi2 = None
        si2 = None
        for i in range(n - 1):
            if not st[i]:
                fi2 = i
                for j in range(i + 1, n):
                    if not st[j]:
                        si2 = j
                        break
                break
        if fi2 is None or si2 is None:
            return True

        st[fi2] = True
        st[si2] = True
        run(points[fi2], points[si2])
        return not (False in st)

    if check(0, 1) or check(0, 2) or check(1, 2):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main(10)