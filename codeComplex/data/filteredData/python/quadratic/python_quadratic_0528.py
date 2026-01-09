def main(n):
    # 生成测试数据：构造一个 n x n 的网格，包含若干 3x3 全 '#' 的块
    # 这里简单生成：在若干位置放置 3x3 的全 '#'，其余为 '.'
    m = n
    a = [["." for _ in range(m)] for _ in range(n)]

    # 简单规则：在若干不重叠的位置放置 3x3 全 '#'
    for i in range(1, n - 1, 4):  # 间隔放置，避免复杂重叠
        for j in range(1, m - 1, 4):
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    ii = i + di
                    jj = j + dj
                    if 0 <= ii < n and 0 <= jj < m:
                        a[ii][jj] = "#"

    # 下面是原逻辑的无 input() 实现
    z = [["." for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if j - 1 >= 0 and j + 1 < m and i + 1 < n and i - 1 >= 0:
                if (a[i - 1][j] == "#" and a[i + 1][j] == "#" and
                    a[i][j - 1] == "#" and a[i][j + 1] == "#" and
                    a[i - 1][j - 1] == "#" and a[i - 1][j + 1] == "#" and
                    a[i + 1][j - 1] == "#" and a[i + 1][j + 1] == "#"):
                    z[i - 1][j] = "#"
                    z[i + 1][j] = "#"
                    z[i][j - 1] = "#"
                    z[i][j + 1] = "#"
                    z[i - 1][j - 1] = "#"
                    z[i - 1][j + 1] = "#"
                    z[i + 1][j - 1] = "#"
                    z[i + 1][j + 1] = "#"

    ff = True
    for i in range(n):
        for j in range(m):
            if z[i][j] != a[i][j]:
                ff = False
                break
        if not ff:
            break

    # print("YES" if ff else "NO")
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改规模
    main(7)