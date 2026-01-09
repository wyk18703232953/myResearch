def main(n):
    # Interpret n as both the size of x and the number of queries m
    if n <= 0:
        return
    x = [i * 2 for i in range(1, n + 1)]
    y = [i for i in range(1, n + 1)]

    m = n
    l = []
    for i in range(m):
        if y[i] in x:
            l.append(x.index(y[i]))
    l.sort()
    output = []
    for i in l:
        output.append(str(x[i]))
    if output:
        # print(" ".join(output))
        pass
if __name__ == "__main__":
    main(5)