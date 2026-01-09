def main(n):
    # Deterministic generation of a, b from n
    # Ensure at least 1
    if n < 4:
        size = 4

    else:
        size = n

    a = (size % 3) + 1
    b = ((size // 2) % 3) + 1

    n = size

    if a > 1 and b > 1:
        # print('NO')
        pass
        return

    if n in [2, 3] and a == 1 and b == 1:
        # print('NO')
        pass
        return

    matrix = [[i in [j + 1, j - 1] for i in range(n)] for j in range(n)]

    a, b = n + 1 - a, n + 1 - b
    if a != n:
        matrix = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i < a and j < a and i != j:
                    matrix[i][j] = True
    elif b != n:
        matrix = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i >= b or j >= b:
                    matrix[i][j] = True
                if i == j:
                    matrix[i][j] = False

    # print('YES')
    pass
    for row in matrix:
        # print("".join('1' if x else '0' for x in row), flush=False)
        pass
if __name__ == "__main__":
    main(10)