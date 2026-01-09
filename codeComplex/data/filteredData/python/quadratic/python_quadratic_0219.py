def main(n):
    # Interpret n as both number of rows and columns for scalability
    rows = n
    cols = n

    # Deterministically generate matrix 'a' with digits [0-9]
    # Each row is a list of integers; digit computed from simple arithmetic
    a = [[(i * cols + j) % 10 for j in range(cols)] for i in range(rows)]

    # Compute column sums
    colsums = [sum(a[i][j] for i in range(rows)) for j in range(cols)]

    # Check rows against column sums
    for row in a:
        if all(rv < sv for (rv, sv) in zip(row, colsums)):
            # print("YES")
            pass
            return

    # print("NO")
    pass
if __name__ == "__main__":
    # Example fixed-scale call for repeatable experiments
    main(5)