from itertools import permutations, chain

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

def main(n):
    # Deterministically generate 3 points based on n
    # Coordinates grow with n to scale the work in get_plots
    points = [
        (0, 0),
        (n, n // 2),
        (n // 2, n)
    ]
    res = solve(points)
    # Keep the original output structure to preserve behavior
    # print(len(res))
    pass
    for x, y in res:
        # print(x, y)
        pass
if __name__ == "__main__":
    main(10)