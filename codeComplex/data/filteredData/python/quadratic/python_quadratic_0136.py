def main(n):
    from itertools import permutations

    # n is the size of each original n x n board (must be >= 1)
    if n <= 0:
        return 0

    # Deterministic test data generator:
    # Generate 4 boards A[0..3], each n x n of '0'/'1' chars, depending on board index and parity.
    A = []
    for k in range(4):
        board = []
        for i in range(n):
            row_chars = []
            for j in range(n):
                # simple deterministic pattern using board index and coordinates
                v = (i + j + k) % 2
                row_chars.append(str(v))
            board.append("".join(row_chars))
        A.append(board)

    P = permutations([0, 1, 2, 3])
    plus = [(0, 0), (0, n), (n, 0), (n, n)]

    tmp = [[0 for _ in range(2 * n)] for _ in range(2 * n)]
    res = 10 ** 17

    for p in P:
        for k in range(4):
            x, y = plus[p[k]]
            for i in range(n):
                row = A[k][i]
                for j in range(n):
                    tmp[i + x][j + y] = int(row[j])

        ans_1 = 0
        ans_2 = 0
        for i in range(2 * n):
            for j in range(2 * n):
                if tmp[i][j] == (i + j) % 2:
                    ans_1 += 1

                else:
                    ans_2 += 1

        if ans_1 < res:
            res = ans_1
        if ans_2 < res:
            res = ans_2

    return res


if __name__ == "__main__":
    # Example deterministic runs for time-complexity experiments
    for size in [1, 2, 4, 8]:
        # print(size, main(size))
        pass