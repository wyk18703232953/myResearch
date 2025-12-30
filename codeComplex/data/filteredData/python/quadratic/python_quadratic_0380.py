def main(n):
    # 这里根据 n 构造一个 n x n 的棋盘，并在其中放若干 'B' 作为测试数据
    # 示例策略：在中间放一个 3x3 的 'B' 方块（若 n < 3，就尽量缩小）
    m = n
    board = [['.' for _ in range(m)] for _ in range(n)]

    # 构造一个以中心为参考的小方块
    size = min(3, n, m)
    if size > 0:
        cx, cy = n // 2, m // 2
        half = size // 2
        for i in range(cx - half, cx - half + size):
            for j in range(cy - half, cy - half + size):
                if 0 <= i < n and 0 <= j < m:
                    board[i][j] = 'B'

    # 以下是原逻辑：在 board 上找出所有 'B' 的最小/最大行列坐标
    minX, minY, maxX, maxY = n, m, 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'B':
                if i < minX:
                    minX = i
                if j < minY:
                    minY = j
                if i > maxX:
                    maxX = i
                if j > maxY:
                    maxY = j

    # 如果没有 'B'，可以约定返回 (None, None) 或其他策略
    if minX == n and minY == m and maxX == 0 and maxY == 0 and board[minX - 1][minY - 1] != 'B':
        return None, None

    # 返回中心坐标（原代码是 1-based 输出）
    return (minX + maxX) // 2 + 1, (minY + maxY) // 2 + 1


if __name__ == "__main__":
    # 示例调用：可自行修改 n 观察结果
    print(main(5))