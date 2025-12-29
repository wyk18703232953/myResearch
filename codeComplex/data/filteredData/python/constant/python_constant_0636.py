import sys
import math
import bisect
import collections

sys.setrecursionlimit(1000000)


def isin(x, y, M):
    return M[0] <= x <= M[2] and M[1] <= y <= M[3]


def solve_one_case(N, M, m1, m2):
    zx = [0, M]
    zx += [m1[0] - 1, m1[2]]
    zx += [m2[0] - 1, m2[2]]
    zx.sort()

    zy = [0, N]
    zy += [m1[1] - 1, m1[3]]
    zy += [m2[1] - 1, m2[3]]
    zy.sort()

    totB = 0
    for i0 in range(5):
        if zx[i0] == zx[i0 + 1]:
            continue
        for i1 in range(5):
            if zy[i1] == zy[i1 + 1]:
                continue

            x0 = zx[i0] + 1
            y0 = zy[i1] + 1
            size = (zx[i0 + 1] - zx[i0]) * (zy[i1 + 1] - zy[i1])

            if isin(x0, y0, m2):
                totB += size
            elif isin(x0, y0, m1):
                pass
            else:
                totB += size // 2
                if size % 2 == 1:
                    if (x0 + y0) % 2 == 1:
                        totB += 1
    return N * M - totB, totB


def generate_test_case(N, M):
    # generate two rectangles m1, m2 inside the board:
    # [x1, y1, x2, y2] with 1-based inclusive coordinates
    # we make them simple and valid
    def clamp(a, lo, hi):
        return max(lo, min(hi, a))

    # m1: roughly central
    x1_1 = max(1, M // 4)
    y1_1 = max(1, N // 4)
    x2_1 = clamp(x1_1 + max(1, M // 4), 1, M)
    y2_1 = clamp(y1_1 + max(1, N // 4), 1, N)
    m1 = [x1_1, y1_1, x2_1, y2_1]

    # m2: another region, shifted
    x1_2 = max(1, (M * 3) // 4 - max(1, M // 4))
    y1_2 = max(1, (N * 3) // 4 - max(1, N // 4))
    x2_2 = clamp(x1_2 + max(1, M // 4), 1, M)
    y2_2 = clamp(y1_2 + max(1, N // 4), 1, N)
    m2 = [x1_2, y1_2, x2_2, y2_2]

    return m1, m2


def main(n):
    """
    n: scale parameter. We generate:
        T = n
        For each test:
            N = 2*n + 1
            M = 2*n + 3
    and output the same format as the original program: one line per test:
        white_cells black_cells
    """
    T = n
    outputs = []
    for _ in range(T):
        N = 2 * n + 1
        M = 2 * n + 3
        m1, m2 = generate_test_case(N, M)
        white, black = solve_one_case(N, M, m1, m2)
        outputs.append(f"{white} {black}")
    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    # example run for some scale, can be changed as needed
    main(3)