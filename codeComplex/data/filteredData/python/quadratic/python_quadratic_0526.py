import random

def main(n):
    # 随机生成一个 n x n 的由 '#' 和 '.' 组成的网格
    m = n
    a = []
    array = []
    for _ in range(n):
        row = []
        # 控制概率：'#' 稍微多一点，方便出现图案
        for _ in range(m):
            row.append('#' if random.random() < 0.6 else '.')
        a.append(row)

    # 初始 array，'#' -> 1, '.' -> 0
    for i in range(n):
        listt = []
        for c in range(m):
            if a[i][c] == '#':
                listt.append(1)
            else:
                listt.append(0)
        array.append(listt)

    # 按原逻辑扫描并减去形成图案的 '#'
    for y in range(1, n - 1):
        for x in range(1, m - 1):
            f = (
                a[y + 1][x] == '#' and
                a[y + 1][x + 1] == '#' and
                a[y + 1][x - 1] == '#'
            )
            s = (
                a[y][x + 1] == '#' and
                a[y][x - 1] == '#'
            )
            th = (
                a[y - 1][x] == '#' and
                a[y - 1][x + 1] == '#' and
                a[y - 1][x - 1] == '#'
            )
            if f and s and th:
                array[y + 1][x]     -= 1
                array[y + 1][x + 1] -= 1
                array[y + 1][x - 1] -= 1
                array[y][x + 1]     -= 1
                array[y][x - 1]     -= 1
                array[y - 1][x - 1] -= 1
                array[y - 1][x]     -= 1
                array[y - 1][x + 1] -= 1

    mb = True
    for y in range(n):
        for x in range(m):
            if array[y][x] == 1:
                mb = False
                break
        if not mb:
            break

    if mb:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：规模 5
    main(5)