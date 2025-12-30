from collections import deque
import random


def signum(n):
    return 1 if n > 0 else 0 if n == 0 else -1


def range_includes(i, j):
    s = signum(j - i)
    return range(i, j + s, s)


def generate_convex_quad():
    """
    生成一个简单的凸四边形的 4 个顶点 (x, y)。
    返回为长度为 8 的列表 [x1,y1,x2,y2,x3,y3,x4,y4]
    """
    # 随机生成四个点，并按 x 再按 y 排序，粗略保证不太退化
    pts = [(random.randint(-10, 10), random.randint(-10, 10)) for _ in range(4)]
    pts = sorted(pts)
    # 转回扁平列表
    flat = []
    for x, y in pts:
        flat.extend([x, y])
    return flat


def main(n):
    """
    n 为规模参数，用于控制随机数据范围（这里简单用于控制坐标范围尺度）。
    返回 True / False。
    """
    random.seed(0)  # 为可复现性固定种子

    # 根据 n 调整坐标范围
    coord_limit = max(5, n)
    def gen_quad_scaled():
        pts = [(random.randint(-coord_limit, coord_limit),
                random.randint(-coord_limit, coord_limit)) for _ in range(4)]
        pts = sorted(pts)
        flat = []
        for x, y in pts:
            flat.extend([x, y])
        return flat

    # 生成两组四边形坐标（各 8 个整数）
    first = gen_quad_scaled()
    second = gen_quad_scaled()

    # 原逻辑开始
    aCoords = tuple(first[i:i + 2] for i in range(0, 8, 2))
    minX = min(aCoord[0] for aCoord in aCoords)
    minY = min(aCoord[1] for aCoord in aCoords)
    maxX = max(aCoord[0] for aCoord in aCoords)
    maxY = max(aCoord[1] for aCoord in aCoords)

    def inFirst(x, y):
        return minX <= x <= maxX and minY <= y <= maxY

    bCoords = tuple(second[i:i + 2] for i in range(0, 8, 2))
    minSum = min(sum(bCoord) for bCoord in bCoords)
    maxSum = max(sum(bCoord) for bCoord in bCoords)
    minDiff = min(bCoord[0] - bCoord[1] for bCoord in bCoords)
    maxDiff = max(bCoord[0] - bCoord[1] for bCoord in bCoords)

    def inSecond(x, y):
        return (minSum <= x + y <= maxSum and
                minDiff <= x - y <= maxDiff)

    for aCoord in aCoords:
        if inSecond(*aCoord):
            return True

    for i in range(-1, 3):
        c1 = bCoords[i]
        c2 = bCoords[i + 1]
        for x, y in zip(range_includes(c1[0], c2[0]),
                        range_includes(c1[1], c2[1])):
            if inFirst(x, y):
                return True

    return False


if __name__ == '__main__':
    # 示例：使用 n = 10 运行
    print("YES" if main(10) else "NO")