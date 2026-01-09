def solve(board):
    n = len(board)
    ans = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'X':
                ans += 2 ** (i * n + j)
    return ans


def reverse_array(arr):
    for row in arr:
        row.reverse()


def rotate(matrix, degree):
    if degree == 0:
        return matrix
    elif degree > 0:
        # rotate 90 degrees clockwise once, then recurse
        return rotate(list(zip(*matrix[::-1])), degree - 90)

    else:
        # rotate 90 degrees counterclockwise once, then recurse
        return rotate(list(zip(*matrix))[::-1], degree + 90)


def make_list(board):
    board = list(board)
    arr = []
    for i in range(len(board)):
        arr.append(list(board[i]))
    return arr


def add_rotations(board, st):
    for _ in range(4):
        st.add(solve(board))
        reverse_array(board)
        st.add(solve(board))
        reverse_array(board)
        board = make_list(rotate(board, 90))


def generate_board(n, pattern_type):
    # 根据 pattern_type 生成不同的测试棋盘
    board = [['.' for _ in range(n)] for _ in range(n)]
    if pattern_type == 0:
        # 全空
        return board
    elif pattern_type == 1:
        # 全 X
        for i in range(n):
            for j in range(n):
                board[i][j] = 'X'
    elif pattern_type == 2:
        # 对角线 X
        for i in range(n):
            board[i][i] = 'X'
    elif pattern_type == 3:
        # 反对角线 X
        for i in range(n):
            board[i][n - 1 - i] = 'X'
    elif pattern_type == 4:
        # 棋盘格
        for i in range(n):
            for j in range(n):
                if (i + j) % 2 == 0:
                    board[i][j] = 'X'

    else:
        # 稀疏 X：每行前半部分
        for i in range(n):
            for j in range(n // 2):
                board[i][j] = 'X'
    return board


def main(n):
    # 生成两个 n×n 的测试棋盘
    # 可以根据需要修改生成逻辑
    arr1 = generate_board(n, 2)  # 例如：对角线 X
    arr2 = generate_board(n, 3)  # 例如：反对角线 X

    s = set()
    s.add(solve(arr1))
    add_rotations(arr1, s)
    l1 = len(s)

    s.add(solve(arr2))
    add_rotations(arr2, s)
    l2 = len(s)

    if l1 == l2:
        # print("Yes")
        pass

    else:
        # print("No")
        pass