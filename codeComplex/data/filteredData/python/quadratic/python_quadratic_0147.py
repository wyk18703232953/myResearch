import random

def main(n):
    # 生成 4 个 n×n 的随机棋盘，每个格子为 '0' 或 '1'
    boards = []
    for _ in range(4):
        board = []
        for _ in range(n):
            row = ''.join(str(random.randint(0, 1)) for _ in range(n))
            board.append(row)
        boards.append(board)

    c = [0] * 4
    for k in range(4):
        for i in range(n):
            s = boards[k][i]
            for j in range(n):
                if (i + j) % 2 != int(s[j]):
                    c[k] += 1

    c.sort()
    result = c[0] + c[1] + 2 * n * n - c[2] - c[3]
    print(result)
    return result

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(4)