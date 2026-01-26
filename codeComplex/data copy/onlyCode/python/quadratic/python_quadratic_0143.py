import itertools

n = int(input())
boards = []
for i in range(4):
    boards.append([])
    for j in range(n):
        boards[-1].append(list(map(int, list(input()))))
    if i < 3: input()

ans = n * n * 4


def check_board(corner, board):
    ans = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] != corner:
                ans += 1
            corner = 1 - corner
    return ans


def solve(corner, p):
    ans = check_board(corner, boards[p[0]])
    ans += check_board(1- corner, boards[p[1]])
    ans += check_board(1 - corner, boards[p[2]])
    ans += check_board(corner, boards[p[3]])

    return ans


for p in itertools.permutations(range(4), 4):
    ans = min(ans, solve(1, p))
    ans = min(ans, solve(0, p))

print(ans)