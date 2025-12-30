import random

def main(n):
    # 生成测试数据：n 行，m 列的网格，随机填充 '*' 和 '.'
    # 为了让规模感更明显，这里让 m 与 n 相同，你可以按需修改生成规则。
    m = n
    # 随机生成一个 n*m 的字符网格
    g = [[random.choice(['*', '.']) for _ in range(m)] for _ in range(n)]

    # 以下是原逻辑，去掉了 input()，直接使用生成的 g、n、m
    c = [[0 for _ in range(m)] for _ in range(n)]

    # 对每一行，计算左右方向上连续 '*' 的最小距离
    for i in range(n):
        v = 0
        for j in range(m):
            v = (v + 1) * (g[i][j] == '*')
            c[i][j] = v
        v = 0
        for j in range(m - 1, -1, -1):
            v = (v + 1) * (g[i][j] == '*')
            c[i][j] = min(c[i][j], v)

    # 对每一列，计算上下方向上连续 '*' 的最小距离
    for j in range(m):
        v = 0
        for i in range(n):
            v = (v + 1) * (g[i][j] == '*')
            c[i][j] = min(c[i][j], v)
        v = 0
        for i in range(n - 1, -1, -1):
            v = (v + 1) * (g[i][j] == '*')
            c[i][j] = min(c[i][j], v)

    # 将值为 1 的位置置 0
    for i in range(n):
        for j in range(m):
            if c[i][j] == 1:
                c[i][j] = 0

    # 按行做扩散覆盖
    for i in range(n):
        v = 0
        for j in range(m):
            v = max(v - 1, c[i][j])
            if v:
                g[i][j] = '.'
        v = 0
        for j in range(m - 1, -1, -1):
            v = max(v - 1, c[i][j])
            if v:
                g[i][j] = '.'

    # 按列做扩散覆盖
    for j in range(m):
        v = 0
        for i in range(n):
            v = max(v - 1, c[i][j])
            if v:
                g[i][j] = '.'
        v = 0
        for i in range(n - 1, -1, -1):
            v = max(v - 1, c[i][j])
            if v:
                g[i][j] = '.'

    # 判断是否完全可覆盖
    if all(g[i][j] == '.' for i in range(n) for j in range(m)):
        r = [(i + 1, j + 1, c[i][j] - 1) for i in range(n) for j in range(m) if c[i][j]]
        print(len(r))
        for t in r:
            print(*t)
    else:
        print(-1)


# 示例调用（在实际评测环境中，评测机会调用 main）
if __name__ == "__main__":
    main(5)