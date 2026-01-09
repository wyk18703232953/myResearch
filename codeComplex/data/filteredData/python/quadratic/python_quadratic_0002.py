def main(n):
    r = 5
    x = [i * 2 for i in range(n)]
    y = [r] * n
    for i in range(1, n):
        for j in range(i):
            d = abs(x[i] - x[j])
            if d <= 2 * r:
                y[i] = max(y[i], y[j] + (4 * r * r - d * d) ** 0.5)
    # print(*y)
    pass
if __name__ == "__main__":
    main(10)