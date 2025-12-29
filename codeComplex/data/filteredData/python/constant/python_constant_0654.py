import sys
import random

sys.setrecursionlimit(1000000)


def dprint(*args, **kwargs):
    # 调试用，如需调试可打开下一行
    # print(*args, file=sys.stderr)
    pass


def getpath(p0, p1):
    if p0[0] < p1[0]:
        sp = 1
    elif p0[0] > p1[0]:
        sp = -1
    else:
        sp = 0
    zz = [tuple(p0), tuple(p1)]
    if sp != 0:
        for x in range(p0[0], p1[0] + sp, sp):
            tp = (x, p0[1])
            zz.append(tp)
    if p0[1] < p1[1]:
        sp = 1
    elif p0[1] > p1[1]:
        sp = -1
    else:
        sp = 0
    if sp != 0:
        for y in range(p0[1], p1[1] + sp, sp):
            tp = (p1[0], y)
            zz.append(tp)
    return zz


def main(n: int):
    """
    n 作为规模参数，用来控制生成的坐标范围：
    三个点 (x, y) 的坐标均在 [-n, n] 内随机生成。
    """
    # 生成三组测试点 p0, p1, p2
    # 确保三点互不相同，避免退化情况
    used = set()
    zp = []
    while len(zp) < 3:
        x = random.randint(-n, n)
        y = random.randint(-n, n)
        if (x, y) in used:
            continue
        used.add((x, y))
        zp.append([x, y])

    p0, p1, p2 = zp
    dprint("Generated points:", p0, p1, p2)

    nr = 1000000
    zr = set()

    for i in range(3):
        for j in range(3):
            cx = zp[i][0]
            cy = zp[j][1]
            cp = (cx, cy)
            z1 = getpath(cp, zp[0])
            z2 = getpath(cp, zp[1])
            z3 = getpath(cp, zp[2])

            z0 = z1 + z2 + z3
            s1 = set(z0)
            dprint(cp, s1)
            if len(s1) < nr:
                nr = len(s1)
                zr = s1

    print(len(zr))
    for x, y in zr:
        print(x, y)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)