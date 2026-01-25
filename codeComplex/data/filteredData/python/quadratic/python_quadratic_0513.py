from math import ceil, sqrt

def main(n):
    # 映射 n 为矩阵规模：n -> (rows, cols)
    # 保证最小为 3x3，避免边界循环退化
    if n < 3:
        n = 3
    rows = n
    cols = n

    # 确定性生成原始矩阵 arr2，由 '#' 和 '.' 组成
    # 这里使用简单的算术模式：根据 (i * cols + j) 的奇偶性决定字符
    arr2 = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = (i * cols + j) % 3
            if val == 0:
                row.append('#')
            else:
                row.append('.')
        arr2.append(row)

    # 原算法逻辑
    arr = [["." for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if (
                arr2[i + 1][j] == arr2[i][j + 1] == arr2[i + 1][j + 1]
                == arr2[i - 1][j] == arr2[i][j - 1] == arr2[i - 1][j - 1]
                == arr2[i + 1][j - 1] == arr2[i - 1][j + 1] == "#"
            ):
                arr[i + 1][j] = arr[i][j + 1] = arr[i + 1][j + 1] = "#"
                arr[i - 1][j] = arr[i][j - 1] = arr[i - 1][j - 1] = "#"
                arr[i + 1][j - 1] = arr[i - 1][j + 1] = "#"

    if arr == arr2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：以 n = 10 作为输入规模运行
    main(10)