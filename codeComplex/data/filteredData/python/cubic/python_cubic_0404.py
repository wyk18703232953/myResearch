import sys
from copy import deepcopy

def main(n):
    # Interpret n as grid size; keep k fixed and even so algorithm runs
    if n <= 0:
        return
    m = n
    k = 4  # fixed even step count for determinism and scalability

    # Deterministic generation of lr and ud based on n, m
    lr = []
    for i in range(n):
        row = [100000001]
        for j in range(m):
            # simple deterministic weight based on i, j
            row.append((i + 1) * (j + 1) % 100 + 1)
        row.append(100000001)
        lr.append(row)

    ud = []
    ud.append([100000001] * m)
    for i in range(n - 1):
        row = []
        for j in range(m):
            row.append((i + j + 2) * 3 % 100 + 1)
        ud.append(row)
    ud.append([100000001] * m)

    if k % 2:
        for _ in range(n):
            sys.stdout.write(" ".join(["-1"] * m) + "\n")
        return

    o = [[1000000001] * (m + 2)]
    for _ in range(n):
        oo = [100000001]
        for _ in range(m):
            oo.append(0)
        oo.append(100000001)
        o.append(oo)
    o.append([100000001] * (m + 2))

    for _ in range(k // 2):
        oo = deepcopy(o)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                oo[i][j] = min(
                    lr[i - 1][j - 1] + o[i][j - 1],
                    lr[i - 1][j] + o[i][j + 1],
                    ud[i - 1][j - 1] + o[i - 1][j],
                    ud[i][j - 1] + o[i + 1][j],
                )
        o = deepcopy(oo)

    for i in o[1 : n + 1]:
        sys.stdout.write(" ".join(map(str, [j * 2 for j in i[1 : m + 1]])) + "\n")


if __name__ == "__main__":
    main(5)