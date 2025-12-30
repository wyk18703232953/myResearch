import random

def main(n):
    # 生成一个 n 行 n 列的随机网格，字符为 '#' 或 '.'
    m = n
    a = []
    for _ in range(n):
        row = []
        for _ in range(m):
            # 可根据需要调整生成比例
            row.append('#' if random.random() < 0.5 else '.')
        a.append(row)

    # 原逻辑
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            may = True
            if (a[i][j - 1] == '.' or a[i][j + 1] == '.' or
                a[i + 1][j - 1] == '.' or a[i + 1][j + 1] == '.' or
                a[i + 1][j] == '.' or
                a[i - 1][j - 1] == '.' or a[i - 1][j + 1] == '.' or
                a[i - 1][j] == '.'):
                may = False
            if may:
                a[i][j - 1] = a[i][j + 1] = \
                a[i + 1][j - 1] = a[i + 1][j + 1] = a[i + 1][j] = \
                a[i - 1][j - 1] = a[i - 1][j + 1] = a[i - 1][j] = '?'

    for i in range(n):
        for j in range(m):
            if a[i][j] == '#':
                print("NO")
                return
    print("YES")


if __name__ == "__main__":
    # 示例：规模为 5，可根据需要修改
    main(5)