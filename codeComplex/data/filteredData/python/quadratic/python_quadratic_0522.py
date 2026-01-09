def transform(c):
    if c == '.':
        return 0
    if c == '#':
        return 1
    return 2

def take_care(board, n, m, N, M):
    if n + 2 >= N:
        return
    if m + 2 >= M:
        return
    if (
        board[n][m + 1] == 0 or
        board[n][m + 2] == 0 or
        board[n + 1][m] == 0 or
        board[n + 1][m + 2] == 0 or
        board[n + 2][m] == 0 or
        board[n + 2][m + 1] == 0 or
        board[n + 2][m + 2] == 0
    ):
        return
    board[n][m] = 2
    board[n][m + 1] = 2
    board[n][m + 2] = 2
    board[n + 1][m] = 2
    board[n + 1][m + 2] = 2
    board[n + 2][m] = 2
    board[n + 2][m + 1] = 2
    board[n + 2][m + 2] = 2
    return False, board

def generate_board(N, M):
    board = []
    for i in range(N):
        row_chars = []
        for j in range(M):
            # Deterministic pattern based on (i + j)
            if (i + j) % 3 == 0:
                row_chars.append('#')

            else:
                row_chars.append('.')
        row = [transform(c) for c in row_chars]
        board.append(row)
    return board

def main(n):
    # Map n to a square board of size N x M where N = M = n
    N = n
    M = n
    board = generate_board(N, M)

    for i in range(N):
        for j in range(M):
            take_care(board, i, j, N, M)

    res = "YES"
    for row in board:
        if 1 in row:
            res = "NO"
            break
    # print(res)
    pass
if __name__ == "__main__":
    main(10)