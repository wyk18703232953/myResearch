import atexit
import io
import sys

_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


def main(n):
    # 生成 4 组棋盘，每组是 n 行长度为 n 的字符串
    boards = []
    for b in range(4):
        board = []
        for k in range(n):
            # 构造一行：按列 j 生成 (k + j + b) % 2
            row = ''.join(str((k + j + b) % 2) for j in range(n))
            board.append(row)
        boards.append(board)

    s = []
    for i in range(4):
        df = 0
        for k in range(n):
            l = boards[i][k]
            for j in range(n):
                if int(l[j]) == (k + j) % 2:
                    df += 1
        s.append(df)

    print(min(
        s[0] + s[1] + n * n - s[2] + n * n - s[3],
        s[0] + s[2] + n * n - s[1] + n * n - s[3],
        s[0] + s[3] + n * n - s[1] + n * n - s[2],
        s[1] + s[2] + n * n - s[0] + n * n - s[3],
        s[1] + s[3] + n * n - s[0] + n * n - s[2],
        s[2] + s[3] + n * n - s[0] + n * n - s[1]
    ))


if __name__ == "__main__":
    # 示例：使用 n = 5 运行
    main(5)