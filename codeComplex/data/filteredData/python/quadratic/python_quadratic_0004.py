import math

def main(n):
    r = 1
    x = [2 * r * i for i in range(n)]
    y = [r]

    for i in range(1, n):
        _y = r
        for j in range(i):
            dx = x[i] - x[j]
            if 4 * r * r >= dx * dx:
                _y = max(_y, y[j] + math.sqrt(4 * r * r - dx * dx))
        y.append(round(_y, 6))

    print(' '.join(map(str, y)))


if __name__ == "__main__":
    main(5)