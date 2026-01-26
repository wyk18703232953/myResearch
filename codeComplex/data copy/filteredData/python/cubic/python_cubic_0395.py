import sys

def main(n):
    # Interpret n as grid size; keep close to original structure
    if n < 2:
        n_rows = 2

    else:
        n_rows = n
    m_cols = n_rows
    # Ensure k is even often enough to exercise main logic; for example 2*n
    k = 2 * n_rows

    # Deterministic construction of A (n x m) and B ((n-1) x m)
    # A[i][j] and B[i][j] are simple functions of indices
    A = [[i * m_cols + j + 1 for j in range(m_cols)] for i in range(n_rows)]
    B = [[(i + 1) * (j + 2) for j in range(m_cols)] for i in range(n_rows - 1)]

    if k % 2 == 0:
        half = k // 2
        INF = 10**12
        O = [[[INF] * m_cols for _ in range(n_rows)] for _ in range(half)]
        for i in range(n_rows):
            for j in range(m_cols):
                if i > 0:
                    O[0][i][j] = min(O[0][i][j], B[i - 1][j])
                if i < n_rows - 1:
                    O[0][i][j] = min(O[0][i][j], B[i][j])
                if j > 0:
                    O[0][i][j] = min(O[0][i][j], A[i][j - 1])
                if j < m_cols - 1:
                    O[0][i][j] = min(O[0][i][j], A[i][j])

        for l in range(1, half):
            prev = O[l - 1]
            cur = O[l]
            for i in range(n_rows):
                for j in range(m_cols):
                    if i > 0:
                        val = B[i - 1][j] + prev[i - 1][j]
                        if val < cur[i][j]:
                            cur[i][j] = val
                    if i < n_rows - 1:
                        val = B[i][j] + prev[i + 1][j]
                        if val < cur[i][j]:
                            cur[i][j] = val
                    if j > 0:
                        val = A[i][j - 1] + prev[i][j - 1]
                        if val < cur[i][j]:
                            cur[i][j] = val
                    if j < m_cols - 1:
                        val = A[i][j] + prev[i][j + 1]
                        if val < cur[i][j]:
                            cur[i][j] = val

        last = O[-1]
        for i in range(n_rows):
            row = [last[i][j] * 2 for j in range(m_cols)]
            # print(*row)
            pass

    else:
        for _ in range(n_rows):
            # print(*([-1] * m_cols))
            pass
if __name__ == "__main__":
    main(5)