# A. Find Square (no input, main(n) with generated test data)

import random

def main(n: int):
    """
    根据规模 n 生成一个 n×n 的棋盘，只含字符 'B' 和 '.'，
    且包含至少一个连续的 'B' 段，然后输出原算法的结果。
    """
    if n <= 0:
        return

    # 先生成全 '.' 的棋盘
    board = [['.' for _ in range(n)] for _ in range(n)]

    # 随机选一行，放置连续 'B'
    row = random.randrange(n)
    # 至少 1 个 B，至多 n 个 B
    length = random.randint(1, n)
    start = random.randint(0, n - length)
    for j in range(start, start + length):
        board[row][j] = 'B'

    # 可选：其他行随机少量 B（保持与原逻辑兼容，不影响首次行匹配）
    for i in range(n):
        if i == row:
            continue
        if random.random() < 0.3:  # 30% 的概率给这一行一些 B
            extra_len = random.randint(1, max(1, n // 3))
            extra_start = random.randint(0, n - extra_len)
            for j in range(extra_start, extra_start + extra_len):
                board[i][j] = 'B'

    # 将棋盘转换为字符串列表，模拟原始输入格式
    lines = [''.join(board[i]) for i in range(n)]

    # 原始逻辑：找到第一行包含 'B' 的行，并输出中心位置
    for i in range(n):
        s = lines[i]
        left = s.find('B')
        if left != -1:
            right = s.rfind('B')
            c = (right - left) // 2 + 1
            # 输出 1-based 坐标（行, 列）
            print(i + c, left + c)
            break


if __name__ == "__main__":
    # 示例：运行 main(8)
    main(8)