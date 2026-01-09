def pre(x, y):
    w = x * (y // 2) + (y % 2) * (x + 1) // 2
    b = x * (y // 2) + (y % 2) * x // 2
    assert w + b == x * y
    return w

def count(x1, y1, x2, y2):
    w = pre(x2, y2) + pre(x1 - 1, y1 - 1) - pre(x2, y1 - 1) - pre(x1 - 1, y2)
    b = (x2 - x1 + 1) * (y2 - y1 + 1) - w
    return w, b

def main(n):
    # n controls the number of test cases and the board / rectangle sizes deterministically
    t = n
    for k in range(1, t + 1):
        # Board dimensions grow with k to give scalable input
        # Ensure minimum size 1x1
        m = max(1, k + 1)          # width
        row_n = max(1, k + 2)      # height

        # First rectangle (white spill candidate)
        x1 = 1
        y1 = 1
        x2 = min(row_n, 1 + k)     # grows with k but bounded by board
        y2 = min(m, 1 + (k // 2))

        # Second rectangle (black spill candidate)
        # Shifted but still inside the board
        x3 = max(1, 1 + (k // 3))
        y3 = max(1, 1 + (k // 4))
        x4 = min(row_n, x3 + (k // 2) + 1)
        y4 = min(m, y3 + (k // 3) + 1)

        # Core logic from original program
        w = pre(m, row_n)
        b = m * row_n - w

        # white spill
        wc, bc = count(x1, y1, x2, y2)
        w -= wc
        b -= bc
        w += (x2 - x1 + 1) * (y2 - y1 + 1)

        # black spill with possible overlap
        if max(x1, x3) <= min(x2, x4) and max(y1, y3) <= min(y2, y4):
            x5 = max(x1, x3)
            y5 = max(y1, y3)
            x6 = min(x2, x4)
            y6 = min(y2, y4)
            w -= (x6 - x5 + 1) * (y6 - y5 + 1)
            wc, bc = count(x5, y5, x6, y6)
            w += wc
            b += bc

        wc, bc = count(x3, y3, x4, y4)
        w -= wc
        b -= bc
        b += (x4 - x3 + 1) * (y4 - y3 + 1)

        # print(w, b)
        pass
if __name__ == "__main__":
    main(5)