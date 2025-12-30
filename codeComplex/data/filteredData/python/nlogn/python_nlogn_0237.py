import random

def main(n):
    # 生成规模为 n 的测试数据：在 [-10^9, 10^9] 范围内随机生成点
    pts = []
    for _ in range(n):
        x = random.randint(-10**9, 10**9)
        y = random.randint(-10**9, 10**9)
        pts.append([x, y])

    if n <= 4:
        print('YES')
        return

    # 第一种尝试：先用 pts[0], pts[1] 确定第一条直线
    b1 = pts[0][0] - pts[1][0]
    a1 = pts[1][1] - pts[0][1]
    c1 = -a1 * pts[0][0] - b1 * pts[0][1]

    a2 = 0
    b2 = 0
    c2 = 1
    p = []
    flag = True

    for i in range(n):
        if (a1 * pts[i][0] + b1 * pts[i][1] + c1 != 0 and
                a2 * pts[i][0] + b2 * pts[i][1] + c2 != 0):
            p.append(pts[i])
            if len(p) == 2:
                b2 = p[0][0] - p[1][0]
                a2 = p[1][1] - p[0][1]
                c2 = -a2 * p[0][0] - b2 * p[0][1]
            if len(p) > 2:
                flag = False
                break

    if flag:
        print("YES")
        return

    # 第二种尝试：第一条直线用 pts[0] 和 P[0]（上一步中剩余的第一个点）
    P = p
    p = [pts[0], P[0]]
    b1 = p[0][0] - p[1][0]
    a1 = p[1][1] - p[0][1]
    c1 = -a1 * p[0][0] - b1 * p[0][1]
    p = []
    a2 = 0
    b2 = 0
    c2 = 1
    flag = True

    for i in range(n):
        if (a1 * pts[i][0] + b1 * pts[i][1] + c1 != 0 and
                a2 * pts[i][0] + b2 * pts[i][1] + c2 != 0):
            p.append(pts[i])
            if len(p) == 2:
                b2 = p[0][0] - p[1][0]
                a2 = p[1][1] - p[0][1]
                c2 = -a2 * p[0][0] - b2 * p[0][1]
            if len(p) > 2:
                flag = False
                break

    if flag:
        print("YES")
        return

    # 第三种尝试：第一条直线用 P[0] 和 pts[1]
    p = [P[0], pts[1]]
    b1 = p[0][0] - p[1][0]
    a1 = p[1][1] - p[0][1]
    c1 = -a1 * p[0][0] - b1 * p[0][1]
    p = []
    a2 = 0
    b2 = 0
    c2 = 1
    flag = True

    for i in range(n):
        if (a1 * pts[i][0] + b1 * pts[i][1] + c1 != 0 and
                a2 * pts[i][0] + b2 * pts[i][1] + c2 != 0):
            p.append(pts[i])
            if len(p) == 2:
                b2 = p[0][0] - p[1][0]
                a2 = p[1][1] - p[0][1]
                c2 = -a2 * p[0][0] - b2 * p[0][1]
            if len(p) > 2:
                flag = False
                break

    if flag:
        print("YES")
        return

    print("NO")