from random import randint

def main(n):
    # 生成一个 n x n 的棋盘，随机放置一些 'B'
    # 若全为空，则强制放置一个 'B'
    m = n
    a = []
    has_B = False

    for _ in range(n):
        row = []
        for _ in range(m):
            # 约 1/4 概率放置 'B'
            if randint(0, 3) == 0:
                row.append('B')
                has_B = True
            else:
                row.append('.')
        a.append(''.join(row))

    if not has_B:
        # 若没有 B，则强制在随机位置放一个
        x = randint(0, n - 1)
        y = randint(0, m - 1)
        row_list = list(a[x])
        row_list[y] = 'B'
        a[x] = ''.join(row_list)

    # 下面是原逻辑
    minx, miny, maxx, maxy = n, m, 0, 0
    for x in range(n):
        for y in range(m):
            if a[x][y] == 'B':
                minx = min(minx, x + 1)
                miny = min(miny, y + 1)
                maxx = max(maxx, x + 1)
                maxy = max(maxy, y + 1)

    cx = (maxx + minx) // 2
    cy = (maxy + miny) // 2
    print(cx, cy)
    return cx, cy

if __name__ == "__main__":
    # 示例：n = 5
    main(5)