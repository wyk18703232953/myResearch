import random

def main(n):
    # 根据规模 n 生成一个 n x n 的随机网格，元素为 '#' 或 '.'
    m = n
    s = []
    for _ in range(n):
        row = []
        for _ in range(m):
            # 适当控制 '#' 的概率，避免太稀或太密
            cell = '#' if random.random() < 0.4 else '.'
            row.append(cell)
        s.append(row)

    # 构造与原程序等价的逻辑
    t = []
    for _ in range(n):
        p = ['.'] * m
        t.append(p)

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            f = 0
            if (
                s[i - 1][j - 1] == '#' and s[i - 1][j] == '#' and s[i - 1][j + 1] == '#' and
                s[i][j - 1] == '#' and s[i][j + 1] == '#' and
                s[i + 1][j - 1] == '#' and s[i + 1][j] == '#' and s[i + 1][j + 1] == '#'
            ):
                f = 1
            if f == 1:
                t[i - 1][j - 1] = '#'
                t[i - 1][j] = '#'
                t[i - 1][j + 1] = '#'
                t[i][j - 1] = '#'
                t[i][j + 1] = '#'
                t[i + 1][j - 1] = '#'
                t[i + 1][j] = '#'
                t[i + 1][j + 1] = '#'

    f = 1
    for i in range(n):
        for j in range(m):
            if s[i][j] == '#' and s[i][j] != t[i][j]:
                f = 0
                break
        if f == 0:
            break

    if f == 1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例调用
    main(5)