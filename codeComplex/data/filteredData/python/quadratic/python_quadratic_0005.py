def main(n):
    # Deterministically generate r and x based on n
    r = max(1, n // 2)
    x = [i for i in range(n)]

    y = [r] * n
    for i in range(n):
        for j in range(i):
            if not (abs(x[i] - x[j]) > 2 * r):
                y[i] = max(y[i], (4 * r ** 2 - (x[i] - x[j]) ** 2) ** 0.5 + y[j])
    for i in y:
        # print(i, end=' ')
        pass
if __name__ == "__main__":
    main(10)