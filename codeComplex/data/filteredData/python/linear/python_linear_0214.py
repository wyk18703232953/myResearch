import io
import sys


def main(n):
    # Deterministically generate a, b based on n
    # Keep them non-trivial but simple
    a = 2
    b = 3

    # Generate n lines of (x, vx, vy)
    # Use simple arithmetic patterns to ensure determinism
    data = []
    for i in range(n):
        x = i
        vx = (i % 5) - 2        # values in [-2, 2]
        vy = (i % 7) - 3        # values in [-3, 3]
        data.append((x, vx, vy))

    dc = {}
    for x, vx, vy in data:
        nx = x + vx
        ny = a * x + b + vy
        dd = a * nx - ny + b
        if dd not in dc:
            dc[dd] = {}
        if (vx, vy) not in dc[dd]:
            dc[dd][(vx, vy)] = 0
        dc[dd][(vx, vy)] += 1

    tot = 0
    for _, k in dc.items():
        tt = 0
        pp = 0
        for _, cc in k.items():
            tt -= cc * (cc + 1) // 2
            pp += cc
        tt += pp * (pp + 1) // 2
        tot += tt * 2

    # print(tot)
    pass
if __name__ == "__main__":
    # Example scale; adjust n for experiments
    main(10_000)