from itertools import permutations, chain

def get_plots(a, b):
    ax, ay = a
    bx, by = b
    step_x = 1 if ax < bx else -1
    for x in range(ax, bx, step_x):
        yield (x, ay)
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
    base_x = n
    base_y = 2 * n + 1
    p1 = (base_x, base_y)
    p2 = (base_x + n, base_y + 1)
    p3 = (base_x + (n // 2 if n > 1 else 1), base_y + 2)
    return [p1, p2, p3]

def main(n):
    points = generate_points(n)
    res = solve(points)
    # print(len(res))
    pass
    for x, y in res:
        # print(x, y)
        pass
if __name__ == "__main__":
    main(10)