def whb(a, b, c, d):
    dim = (c - a + 1) * (d - b + 1)
    col1 = dim // 2
    col2 = dim - col1
    if (a + b) % 2 == 0:
        return [col2, col1]

    else:
        return [col1, col2]


def insegment(a, b, a1, b1):
    li = [[a, 1], [b, 1], [a1, 2], [b1, 2]]
    li.sort()
    if li[0][1] == li[1][1]:
        if li[1][0] == li[2][0]:
            return [li[1][0], li[2][0]]

        else:
            return -1

    else:
        return [li[1][0], li[2][0]]


def inrect(a, b, c, d, a1, b1, c1, d1):
    xra = insegment(a, c, a1, c1)
    yra = insegment(b, d, b1, d1)
    if xra == -1 or yra == -1:
        return -1

    else:
        return [xra[0], yra[0], xra[1], yra[1]]


def main(n):
    q = n
    results = []
    for quer in range(q):
        # Board size grows with n, but also depends on query index for variability
        N = n + quer + 1
        M = n + (quer % (n + 1)) + 1

        # First rectangle: roughly central, size scales with n
        x1 = max(1, N // 4)
        y1 = max(1, M // 4)
        x2 = min(N, x1 + max(1, n // 3))
        y2 = min(M, y1 + max(1, n // 4))

        # Second rectangle: shifted, may overlap
        x3 = max(1, N // 3)
        y3 = max(1, M // 3)
        x4 = min(N, x3 + max(1, n // 2))
        y4 = min(M, y3 + max(1, n // 5))

        white, black = whb(1, 1, N, M)
        w1, b1 = whb(x1, y1, x2, y2)
        w2, b2 = whb(x3, y3, x4, y4)

        black += w2 - b1
        white += b1 - w2

        inter = inrect(x1, y1, x2, y2, x3, y3, x4, y4)
        if isinstance(inter, list):
            w3, b3 = whb(inter[0], inter[1], inter[2], inter[3])
            black += b3
            white -= b3

        results.append((white, black))

    for w, b in results:
        # print(w, b)
        pass
if __name__ == "__main__":
    main(10)