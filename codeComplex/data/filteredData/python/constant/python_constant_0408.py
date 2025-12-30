import random

def inn1(s1, xmi1, xma1, ymi1, yma1, c2):
    t = False
    for i in s1:
        if xmi1 <= i[0] <= xma1 and ymi1 <= i[1] <= yma1:
            t = True
            break
    if xmi1 <= c2[0] <= xma1 and ymi1 <= c2[1] <= yma1:
        t = True
    return t

def inn2(s, xmi2, xma2, ymi2, yma2, c1):
    t = False
    for i in s:
        if xmi2 <= i[0] <= xma2 and ymi2 <= i[1] <= yma2:
            t = True
            break
    if xmi2 <= c1[0] <= xma2 and ymi2 <= c1[1] <= yma2:
        t = True
    return t

def conv(s):
    for i in range(4):
        x = s[i][0]
        y = s[i][1]
        s[i][0] = x + y
        s[i][1] = x - y
    return s

def compute_bounds(s, s1):
    xma1 = s[0][0]
    xma2 = s1[0][0]
    xmi1 = s[0][0]
    xmi2 = s1[0][0]
    yma1 = s[0][1]
    yma2 = s1[0][1]
    ymi1 = s[0][1]
    ymi2 = s1[0][1]
    for i in range(4):
        xma1 = max(xma1, s[i][0])
        xma2 = max(xma2, s1[i][0])
        xmi1 = min(xmi1, s[i][0])
        xmi2 = min(xmi2, s1[i][0])
        yma1 = max(yma1, s[i][1])
        yma2 = max(yma2, s1[i][1])
        ymi1 = min(ymi1, s[i][1])
        ymi2 = min(ymi2, s1[i][1])
    return xmi1, xma1, ymi1, yma1, xmi2, xma2, ymi2, yma2

def main(n):
    # n 用来控制测试数据规模，这里用于控制坐标范围
    coord_min = -n
    coord_max = n

    # 生成两组四边形顶点：s 和 s1，每个四边形 4 个点
    s = [[random.randint(coord_min, coord_max),
          random.randint(coord_min, coord_max)] for _ in range(4)]
    s1 = [[random.randint(coord_min, coord_max),
           random.randint(coord_min, coord_max)] for _ in range(4)]

    # 初始边界与中心
    xmi1, xma1, ymi1, yma1, xmi2, xma2, ymi2, yma2 = compute_bounds(s, s1)
    c1 = [(xma1 + xmi1) / 2, (yma1 + ymi1) / 2]
    c2 = [(xma2 + xmi2) / 2, (yma2 + ymi2) / 2]

    st = set()
    for i in s:
        st.add(i[1])
    t = (len(st) == 2)

    if t:
        t1 = inn1(s1, xmi1, xma1, ymi1, yma1, c2)
        s = conv(s)
        s1 = conv(s1)
        xmi1, xma1, ymi1, yma1, xmi2, xma2, ymi2, yma2 = compute_bounds(s, s1)
        c1 = [(xma1 + xmi1) / 2, (yma1 + ymi1) / 2]
        c2 = [(xma2 + xmi2) / 2, (yma2 + ymi2) / 2]
        t2 = inn2(s, xmi2, xma2, ymi2, yma2, c1)
    else:
        t1 = inn2(s, xmi2, xma2, ymi2, yma2, c1)
        s = conv(s)
        s1 = conv(s1)
        xmi1, xma1, ymi1, yma1, xmi2, xma2, ymi2, yma2 = compute_bounds(s, s1)
        c1 = [(xma1 + xmi1) / 2, (yma1 + ymi1) / 2]
        c2 = [(xma2 + xmi2) / 2, (yma2 + ymi2) / 2]
        t2 = inn1(s1, xmi1, xma1, ymi1, yma1, c2)

    if t1 or t2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：使用 n=100 生成测试数据运行
    main(100)