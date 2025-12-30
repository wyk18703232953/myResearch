from itertools import permutations, chain
import random

def get_plots(a, b):
    ax, ay = a
    bx, by = b

    if ax != bx:
        step_x = 1 if ax < bx else -1
        for x in range(ax, bx, step_x):
            yield (x, ay)
    if ay != by:
        step_y = 1 if ay < by else -1
        for y in range(ay, by, step_y):
            yield (bx, y)

def solve(points):
    for a, b, c in permutations(points):
        ax, ay = a
        bx, by = b
        cx, cy = c
        if min(ax, bx) <= cx <= max(ax, bx) and min(ay, by) <= cy <= max(ay, by):
            return list(chain(get_plots(a, c), get_plots(c, b), [b]))

    def it():
        for a, b, c in permutations(points):
            ax, ay = a
            bx, by = b
            m = (ax, by)
            L = list(chain(get_plots(a, m), get_plots(b, m), get_plots(c, m), [m]))
            yield (len(L), L)

    return min(it())[1]

def generate_points(n):
    # 生成 3 个点，坐标范围根据 n 调整
    # 范围 [-n, n]
    pts = set()
    while len(pts) < 3:
        x = random.randint(-n, n)
        y = random.randint(-n, n)
        pts.add((x, y))
    return list(pts)

def main(n):
    points = generate_points(n)
    res = solve(points)
    print(len(res))
    for x, y in res:
        print(x, y)

if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    main(10)