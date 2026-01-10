import sys
from math import *

def generate_data(n):
    # 映射规则：
    # n >= 2 时：
    #   n 视为垂直和水平线段的总规模
    #   n_v = n // 2 条垂直线
    #   n_h = n - n_v 条水平线
    # n < 2 时，退化为至少 1 条垂直线，0 条水平线
    if n < 2:
        n_v = 1
        n_h = 0
    else:
        n_v = n // 2
        n_h = n - n_v

    # 生成垂直线的 x 坐标：vert 列表
    # 使用简单确定性公式：x = 1 + i*2
    vert = [1 + i * 2 for i in range(n_v)]

    # 生成水平线：三元组 (y, x1, x2)
    # y = 1 + i，x1 固定为 1，使得条件 (i[1] == 1) 能被触发
    # x2 = 2 + (i % (n_v + 1))，保证范围有一定变化
    horiz = []
    for i in range(n_h):
        y = 1 + i
        x1 = 1
        x2 = 2 + (i % (n_v + 1))
        horiz.append((y, x1, x2))

    return n_v, n_h, vert, horiz

def main(n):
    n_v, n_h, vert, horiz = generate_data(n)

    vert.sort()
    horiz.sort()

    p = -1
    hh = []
    for seg in horiz:
        if p != seg[0]:
            p = seg[0]
            if seg[1] == 1:
                hh.append(seg[2])

    hh.sort()
    i = 0
    hl = len(hh)
    vl = len(vert)
    r = n_v + n_h
    for j in range(vl):
        while i < hl and hh[i] < vert[j]:
            i += 1
        r = min(r, hl - i + j)
    while i < hl and hh[i] < 1000000000:
        i += 1
    r = min(r, hl - i + vl)
    print(r)

if __name__ == "__main__":
    # 示例：使用 n = 10 作为输入规模进行一次运行
    main(10)