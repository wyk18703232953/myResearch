import math
from itertools import product

def main(n):
    n_rows = n
    m_cols = n
    k_steps = 2 * n if n > 0 else 0

    if k_steps % 2 == 1 or n_rows == 0 or m_cols == 0:
        for _ in range(n_rows):
            # print(" ".join(["-1"] * m_cols))
            pass
        return

    horiz_costs = [[(i + j) % 7 + 1 for j in range(m_cols - 1)] for i in range(n_rows)]
    vert_costs = [[(i * 3 + j * 5) % 9 + 1 for j in range(m_cols)] for i in range(n_rows - 1)]

    ans = [[[0] * m_cols for _ in range(n_rows)] for _ in range(k_steps // 2 + 1)]

    def costs(i, j, time):
        r = []
        if j < m_cols - 1:
            r.append(2 * horiz_costs[i][j] + ans[time - 1][i][j + 1])
        if j > 0:
            r.append(2 * horiz_costs[i][j - 1] + ans[time - 1][i][j - 1])
        if i < n_rows - 1:
            r.append(2 * vert_costs[i][j] + ans[time - 1][i + 1][j])
        if i > 0:
            r.append(2 * vert_costs[i - 1][j] + ans[time - 1][i - 1][j])
        return r

    for time in range(1, k_steps // 2 + 1):
        for i in range(n_rows):
            for j in range(m_cols):
                cost_list = costs(i, j, time)
                best = 0
                for c in cost_list:
                    if best == 0 or c < best:
                        best = c
                ans[time][i][j] = best

    for i in range(n_rows):
        # print(" ".join(str(s) for s in ans[-1][i]))
        pass
if __name__ == "__main__":
    main(5)