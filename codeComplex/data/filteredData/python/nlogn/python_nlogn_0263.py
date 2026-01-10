def main(n):
    # Generate deterministic data:
    # Original input: n lines, each with two integers.
    # Here we generate pairs (x, y) based on i and n.
    a = []
    for i in range(n):
        x = i % (n // 2 + 1)  # ensures some equal first elements when n large
        y = (i * 2 + 3) % (n + 5)
        a.append([x, y, i + 1])

    a.sort(key=lambda e: e[0])
    f = 0
    if n >= 2:
        for i in range(n - 1):
            if a[i][0] == a[i + 1][0]:
                if a[i][1] >= a[i + 1][1]:
                    print(a[i + 1][2], a[i][2])
                else:
                    print(a[i][2], a[i + 1][2])
                f = 1
                break
            if a[i][1] >= a[i + 1][1]:
                f = 1
                print(a[i + 1][2], a[i][2])
                break
    if f == 0:
        print(-1, -1)


if __name__ == "__main__":
    main(10)