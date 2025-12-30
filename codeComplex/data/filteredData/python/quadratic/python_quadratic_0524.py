import random

def main(n):
    # 生成测试数据：n 行，每行 n 列，随机由 '.' 和 '#' 组成
    m = n
    cl = []
    for _ in range(n):
        row = ''.join(random.choice(['.', '#']) for _ in range(m))
        cl.append(row)

    def is_squad(x, y):
        return (
            cl[x][y] == '#' and
            cl[x + 1][y] == '#' and
            cl[x + 2][y] == '#' and
            cl[x + 2][y + 1] == '#' and
            cl[x + 2][y + 2] == '#' and
            cl[x + 1][y + 2] == '#' and
            cl[x][y + 2] == '#' and
            cl[x][y + 1] == '#'
        )

    def cv(x, y):
        if x - 2 >= 0 and y + 2 <= m - 1 and is_squad(x - 2, y):
            return True
        elif x - 1 >= 0 and x + 1 <= n - 1 and y + 2 <= m - 1 and is_squad(x - 1, y):
            return True
        elif x + 2 <= n - 1 and y + 2 <= m - 1 and is_squad(x, y):
            return True
        elif x + 2 <= n - 1 and y + 1 <= m - 1 and y - 1 >= 0 and is_squad(x, y - 1):
            return True
        elif x + 2 <= n - 1 and y - 2 >= 0 and is_squad(x, y - 2):
            return True
        elif x + 1 <= n - 1 and x - 1 >= 0 and y - 2 >= 0 and is_squad(x - 1, y - 2):
            return True
        elif x - 2 >= 0 and y - 2 >= 0 and is_squad(x - 2, y - 2):
            return True
        elif x - 2 >= 0 and y - 1 >= 0 and y + 1 <= m - 1 and is_squad(x - 2, y - 1):
            return True
        else:
            return False

    for i in range(n):
        for j in range(m):
            if cl[i][j] == '#':
                if not cv(i, j):
                    print('NO')
                    return

    print('YES')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)