import sys


def generate_input(n):
    # Deterministically generate (n, a, b) and n lines of (x, vx, vy)
    # Choose a, b based on n
    a = n % 10 + 1
    b = (n // 2) % 10

    data = []
    data.append(f"{n} {a} {b}")
    for i in range(n):
        x = i
        vx = (i * 2 + 1) % (n + 3)
        vy = (i * 3 + 2) % (n + 5)
        data.append(f"{x} {vx} {vy}")
    return data


def compute(lines):
    it = iter(lines)
    n, a, b = [int(x) for x in next(it).split()]
    dc = {}
    for _ in range(n):
        x, vx, vy = [int(x) for x in next(it).split()]
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
    return tot


def main(n):
    lines = generate_input(n)
    result = compute(lines)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)