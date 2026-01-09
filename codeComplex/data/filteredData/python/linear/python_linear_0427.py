def main(n):
    # Generate deterministic data
    # Each of n rows has length equal to n, values based on i and j
    data = []
    for i in range(n):
        row = [(i + 1) * (j + 1) for j in range(n)]
        data.append(row)

    a = []
    t = None
    for i in range(n):
        l_sum = sum(data[i])
        if i == 0:
            t = l_sum
        a.append(l_sum)

    a.sort(reverse=True)
    # print(a.index(t) + 1)
    pass
if __name__ == "__main__":
    main(10)