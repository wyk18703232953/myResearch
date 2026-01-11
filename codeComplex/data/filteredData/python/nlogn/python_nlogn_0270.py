def main(n):
    # Generate deterministic input data:
    # Original input structure: n lines, each with 2 integers
    # Here we define a[i] = [i % (n // 2 + 1), (i * 2) % (n + 3)]
    a = [[i % (n // 2 + 1), (i * 2) % (n + 3)] for i in range(n)]

    for t in range(n):
        a[t].append(t + 1)
    a.sort()
    for i in range(n - 1):
        if a[i][1] >= a[i + 1][1]:
            # print(a[i + 1][2], a[i][2])
            pass
            return
        if a[i][0] == a[i + 1][0] and a[i][1] <= a[i + 1][1]:
            # print(a[i][2], a[i + 1][2])
            pass
            return
    # print(-1, -1)
    pass
if __name__ == "__main__":
    main(10)