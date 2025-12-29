import random
import string

def main(n: int):
    # 生成测试数据：4 个大小为 n*n 的棋盘，只含 'B' 和 'W'
    def gen_board(size):
        return [
            ''.join(random.choice('BW') for _ in range(size))
            for _ in range(size)
        ]

    chess = [gen_board(n) for _ in range(4)]

    issue = {0: 0, 1: 0, 2: 0, 3: 0}
    reversed_issue = {0: 0, 1: 0, 2: 0, 3: 0}

    for w in range(4):
        # 将四个棋盘合成为 2n * 2n 的棋盘
        chessdesk = [chess[0] + chess[3]] + [chess[1] + chess[2]]
        for s in range(2 * n):
            chessdesk[0][s] += chessdesk[1][s]
        chessdesk.pop(1)
        chessdesk = chessdesk[0]
        colour = chessdesk[0][0]

        # 统计与标准棋盘的差异
        for i in range(2 * n):
            for j in range(2 * n):
                if (i + j) % 2 == 0:
                    if chessdesk[i][j] != colour:
                        issue[w] += 1
                else:
                    if chessdesk[i][j] == colour:
                        issue[w] += 1

        reversed_issue[w] = 4 * n ** 2 - issue[w]

        # 轮流交换棋盘的位置
        if w == 0:
            chess[0], chess[3] = chess[3], chess[0]
        elif w == 1:
            chess[1], chess[3] = chess[3], chess[1]
        elif w == 2:
            chess[1], chess[2] = chess[2], chess[1]

    result = min(min(issue.values()), min(reversed_issue.values()))
    print(result)


if __name__ == "__main__":
    # 示例：n = 5，可根据需要修改
    main(5)