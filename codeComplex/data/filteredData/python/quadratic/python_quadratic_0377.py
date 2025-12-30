# A. Find Square - main(n) version with generated test data

import random

def generate_test_data(n):
    # 随机生成一个 n x n 的矩阵，包含一个连续的 'B' 正方形
    # 其余位置为 'W'
    matrix = [['W'] * n for _ in range(n)]

    # 正方形边长，至少 1，至多 n
    side = random.randint(1, n)
    # 左上角坐标，保证方块完全在矩阵内
    top_row = random.randint(0, n - side)
    left_col = random.randint(0, n - side)

    # 填充 'B' 方块
    for i in range(top_row, top_row + side):
        for j in range(left_col, left_col + side):
            matrix[i][j] = 'B'

    # 转成字符串形式
    return [''.join(row) for row in matrix], side, top_row, left_col


def main(n):
    # 生成测试数据
    matrix, side, top_row, left_col = generate_test_data(n)

    # 模拟原始代码逻辑，寻找所有 'B' 所在的最小包围矩形的中心
    top = [-1, -1]
    bottom = [-1, -1]

    # 找到最上面一行出现 'B' 的位置
    for i in range(n):
        left = matrix[i].find('B')
        if left != -1:
            top[0] = i
            top[1] = left
            break

    # 找到最下面一行出现 'B' 的位置
    for i in range(n - 1, -1, -1):
        right = matrix[i].rfind('B')
        if right != -1:
            bottom[0] = i
            bottom[1] = right
            break

    # 根据题目要求输出 1-based 坐标
    row_center = 1 + top[0] + (bottom[0] - top[0]) // 2
    col_center = 1 + top[1] + (bottom[1] - top[1]) // 2
    print(row_center, col_center)

    # 若需要调试，可打印生成的矩阵和方块信息：
    # for row in matrix:
    #     print(row)
    # print("side:", side, "top_row:", top_row + 1, "left_col:", left_col + 1)


if __name__ == "__main__":
    # 示例：规模 n = 8
    main(8)