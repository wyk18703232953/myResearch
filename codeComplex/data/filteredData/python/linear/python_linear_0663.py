def main(n):
    # Deterministically generate s based on n
    s = n * (n + 1) // 2

    # Initialize degree list
    l = [0 for _ in range(n)]

    # Deterministically generate a tree with n nodes using a simple pattern:
    # Connect node i with node (i+1) to form a path (1-2-3-...-n)
    # which is a valid tree structure
    for i in range(n - 1):
        a = i + 1
        b = i + 2
        l[a - 1] += 1
        l[b - 1] += 1

    count = 0
    for i in range(n):
        if l[i] == 1:
            count += 1

    if count == 0:
        result = 0

    else:
        result = (s / count) * 2
    # print(result)
    pass
if __name__ == "__main__":
    main(10)