def main(n):
    # Interpret n as both the length of x and y
    if n <= 0:
        return
    # Deterministic construction of x and y
    x = [i for i in range(n)]
    y = [(i * 2) % n for i in range(n)]
    m = len(y)

    l = []
    for i in range(m):
        for j in range(n):
            if y[i] == x[j]:
                l.append(j)
    result = ' '.join(map(str, [x[i] for i in sorted(l)]))
    # print(result)
    pass
if __name__ == "__main__":
    main(10)