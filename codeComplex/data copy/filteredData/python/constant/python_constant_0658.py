def main(n):
    # Generate deterministic input data based on n
    # Each of a, b, c is a list of two integers like original usage [x, y]
    # Use n to scale coordinates so complexity grows with n
    a = [0, 0]
    b = [n, n // 2]
    c = [n // 2, n]

    a, b, c = sorted([a, b, c])

    path = []
    for i in range(min(a[1], b[1], c[1]), max(a[1], b[1], c[1]) + 1):
        path.append((b[0], i))
    for i in range(a[0], b[0] + 1):
        path.append((i, a[1]))
    for i in range(b[0], c[0] + 1):
        path.append((i, c[1]))

    unique_path = list(set(path))
    # print(len(unique_path))
    pass
    for x, y in unique_path:
        # print(x, y)
        pass
if __name__ == "__main__":
    main(10)