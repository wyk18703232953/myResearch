import sys
import io


def main(n):
    # Deterministic parameter generation based on n
    a = 2
    b = 3

    dc = {}
    for i in range(n):
        # Deterministic generation of x, vx, vy from index i and n
        x = i
        vx = (i * 2 + 1) % (n + 3)
        vy = (i * 3 + 2) % (n + 5)

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
    print(tot)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)