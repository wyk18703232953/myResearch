def solve(board):
    n = len(board)
    ans = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'X':
                ans += 2 ** (i * n + j)
    return ans


def reverse_array(arr):
    for i in range(len(arr)):
        arr[i].reverse()


def rotate(matrix, degree):
    if degree == 0:
        return matrix
    elif degree > 0:
        return rotate(zip(*matrix[::-1]), degree - 90)

    else:
        return rotate(zip(*matrix)[::-1], degree + 90)


def make_list(board):
    board = list(board)
    arr = []
    for i in range(len(list(board))):
        arr.append(list(board[i]))
    return arr


def add_rotations(board, st):
    for _ in range(4):
        st.add(solve(board))
        reverse_array(board)
        st.add(solve(board))
        reverse_array(board)
        board = make_list(rotate(board, 90))


def generate_board(n, offset):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            # Deterministic pattern: toggle 'X' based on (i * n + j + offset)
            if ((i * n + j + offset) % 3) == 0:
                row.append('X')

            else:
                row.append('.')
        board.append(row)
    return board


def main(n):
    # n is the board size; original program had an n x n board and two boards
    arr1 = generate_board(n, 0)
    arr2 = generate_board(n, n * n // 2)

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
if __name__ == "__main__":
    main(5)