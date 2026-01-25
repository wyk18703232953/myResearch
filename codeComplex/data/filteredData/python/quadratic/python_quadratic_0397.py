def main(n):
    # Interpret n as the size of an n x n grid
    rows = n
    cols = n

    # Deterministic grid generation:
    # Place a contiguous block of 'B's forming a square-ish region whose
    # corners depend deterministically on n.
    M = [['0' for _ in range(cols)] for _ in range(rows)]

    # Define the top-left corner and side length of the B-square deterministically
    if n == 0:
        # Degenerate case: nothing to print or process
        return

    side = max(1, n // 3)
    top = n // 4
    left = n // 5
    bottom = min(rows, top + side) - 1
    right = min(cols, left + side) - 1

    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            M[i][j] = 'B'

    # Original algorithm logic
    start = []
    end = []
    for a in range(rows):
        for b in range(cols):
            if M[a][b] == 'B':
                if not start:
                    start.append(a + 1)
                    start.append(b + 1)
                else:
                    end.clear()
                    end.append(a + 1)
                    end.append(b + 1)

    if not start or not end:
        print(start[0], start[1])
    else:
        mid1 = int((end[0] + start[0]) / 2)
        mid2 = int((end[1] + start[1]) / 2)
        print(mid1, mid2)


if __name__ == "__main__":
    # Example deterministic call; change n to probe different input scales
    main(10)