def main(n):
    # Interpret n as both the number of rows and columns of the grid
    rows = n
    cols = n

    # Deterministically generate arr2: a pattern of '#' and '.' based on indices
    # For example, make a checkerboard-like pattern with some structure
    arr2 = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # Simple deterministic rule: place '#' when (i*j) % 3 == 0 and not on border,
            # otherwise '.'. This ensures some interior '#' cells.
            if 0 < i < rows - 1 and 0 < j < cols - 1 and (i * j) % 3 == 0:
                row.append("#")

            else:
                row.append(".")
        arr2.append(row)

    # Initialize arr as in the original code
    arr = [["." for _ in range(cols)] for _ in range(rows)]

    # Core algorithm logic (unchanged except for using generated data)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if (
                arr2[i + 1][j] == arr2[i][j + 1] == arr2[i + 1][j + 1]
                == arr2[i - 1][j] == arr2[i][j - 1] == arr2[i - 1][j - 1]
                == arr2[i + 1][j - 1] == arr2[i - 1][j + 1] == "#"
            ):
                arr[i + 1][j] = "#"
                arr[i][j + 1] = "#"
                arr[i + 1][j + 1] = "#"
                arr[i - 1][j] = "#"
                arr[i][j - 1] = "#"
                arr[i - 1][j - 1] = "#"
                arr[i + 1][j - 1] = "#"
                arr[i - 1][j + 1] = "#"

    if arr == arr2:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(10)