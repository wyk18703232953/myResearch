def main(n):
    # n: number of points
    if n <= 0:
        # print()
        pass
        return
    r = 1
    x = [i for i in range(n)]
    y = [r] * n
    for i in range(1, n):
        for j in range(i):
            d = abs(x[i] - x[j])
            if d <= 2 * r:
                val = (4 * r * r - d * d) ** 0.5
                if y[j] + val > y[i]:
                    y[i] = y[j] + val
    # print(*y)
    pass
if __name__ == "__main__":
    main(10)