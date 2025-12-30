import random

def main(n):
    # 随机生成一个 n x n 的网格，包含 '.' 和 '*'
    # 为了保证有一些星号，这里设定星号概率为 30%
    m = n
    p_star = 0.3
    grid = []
    for _ in range(n):
        row_str = ''.join('*' if random.random() < p_star else '.' for _ in range(m))
        grid.append(row_str)

    # 下面是原逻辑，去掉了所有 input() / 特殊 IO 包装，直接使用内存中的 grid

    row = [[[] for _ in range(m)] for _ in range(n)]
    col = [[[] for _ in range(m)] for _ in range(n)]
    visr = [[-1 for _ in range(m)] for _ in range(n)]
    visc = [[-1 for _ in range(m)] for _ in range(n)]
    out = []
    all_star = 0

    # 预处理每一行连续的 '*' 段
    for i in range(n):
        be, en = -1, -1
        for j in range(m):
            if grid[i][j] == '*':
                en += 1
                if be == -1:
                    be = en = j
            else:
                if be != -1:
                    for k in range(be, en + 1):
                        row[i][k] = [be, en]
                be = -1
        if be != -1:
            for k in range(be, en + 1):
                row[i][k] = [be, en]

    # 预处理每一列连续的 '*' 段
    for i in range(m):
        be, en = -1, -1
        for j in range(n):
            if grid[j][i] == '*':
                en += 1
                if be == -1:
                    be = en = j
            else:
                if be != -1:
                    for k in range(be, en + 1):
                        col[k][i] = [be, en]
                be = -1
        if be != -1:
            for k in range(be, en + 1):
                col[k][i] = [be, en]

    # 枚举每个 '*' 作为十字中心
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                all_star += 1
                # 水平方向左右最小距离
                hor = min(row[i][j][1] - j, j - row[i][j][0])
                # 垂直方向上下最小距离
                ver = min(col[i][j][1] - i, i - col[i][j][0])
                # 使得十字的臂长在两个方向一致
                if hor <= ver:
                    ver = hor
                else:
                    hor = ver
                if hor > 0 and ver > 0:
                    out.append('%d %d %d' % (i + 1, j + 1, hor))
                    # 标记本十字覆盖的水平线段和竖直线段的端点
                    visr[i][j - ver] = j + ver
                    visc[i - hor][j] = i + hor

    # 统计被覆盖到的 '*' 坐标
    dis = set()
    for i in range(n):
        j, ma = 0, -1
        while j < m:
            ma = max(ma, visr[i][j])
            if ma >= j:
                dis.add((i, j))
            j += 1

    for i in range(m):
        j, ma = 0, -1
        while j < n:
            ma = max(ma, visc[j][i])
            if ma >= j:
                dis.add((j, i))
            j += 1

    # 构造输出字符串并返回
    if len(dis) != all_star:
        return "-1"
    else:
        return '%d\n%s' % (len(out), '\n'.join(out))


# 简单示例调用
if __name__ == "__main__":
    # 自行修改 n 以测试不同规模
    result = main(5)
    print(result)