import math

def main(n):
    # n: number of points
    if n <= 0:
        return

    r = 1
    x = [i for i in range(n)]
    y = [r]

    for i in range(1, n):
        _y = r
        for j in range(i):
            dx = x[i] - x[j]
            if 4 * r * r >= dx * dx:
                _y = max(_y, y[j] + math.sqrt(4 * r * r - dx * dx))
        y.append(_y)

    # print(' '.join(map(str, y)))
    pass
if __name__ == "__main__":
    main(10)