def main(n):
    import itertools

    # Deterministic board generation based on n
    boards = []
    for b in range(4):
        board = []
        for i in range(n):
            row = [((i * n + j + b) % 2) for j in range(n)]
            board.append(row)
        boards.append(board)

    def check_board(corner, board):
        cnt = 0
        current = corner
        for i in range(n):
            for j in range(n):
                if board[i][j] != current:
                    cnt += 1
                current = 1 - current
        return cnt

    def solve(corner, p):
        res = check_board(corner, boards[p[0]])
        res += check_board(1 - corner, boards[p[1]])
        res += check_board(1 - corner, boards[p[2]])
        res += check_board(corner, boards[p[3]])
        return res

    ans = n * n * 4
    for p in itertools.permutations(range(4), 4):
        ans = min(ans, solve(1, p))
        ans = min(ans, solve(0, p))

    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    main(5)