import math

def main(n):
    # Interpret n as number of points
    # Deterministically generate r and x:
    # r is fixed positive radius
    r = 10
    # x is a list of n integers with some spacing pattern
    # Example: arithmetic progression with step 3
    x = [3 * i for i in range(n)]

    y = [r]

    for i in range(1, n):
        _y = r
        for j in range(i):
            dx = x[i] - x[j]
            if 4 * r * r >= dx * dx:
                _y = max(_y, y[j] + math.sqrt(4 * r * r - dx * dx))
        y.append(round(_y, 6))

    # print(' '.join(map(str, y)))
    pass
if __name__ == "__main__":
    main(5)