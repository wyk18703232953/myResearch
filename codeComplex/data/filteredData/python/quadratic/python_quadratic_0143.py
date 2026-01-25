import itertools

n_global = 0
boards = []


def check_board(corner, board, n):
    ans = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] != corner:
                ans += 1
            corner = 1 - corner
    return ans


def solve(corner, p, n):
    ans = check_board(corner, boards[p[0]], n)
    ans += check_board(1 - corner, boards[p[1]], n)
    ans += check_board(1 - corner, boards[p[2]], n)
    ans += check_board(corner, boards[p[3]], n)
    return ans


def generate_boards(n):
    bds = []
    for k in range(4):
        board = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append((i + j + k) % 2)
            board.append(row)
        bds.append(board)
    return bds


def main(n):
    global n_global, boards
    n_global = n
    boards = generate_boards(n)
    ans = n * n * 4
    for p in itertools.permutations(range(4), 4):
        ans = min(ans, solve(1, p, n))
        ans = min(ans, solve(0, p, n))
    print(ans)


if __name__ == "__main__":
    main(5)