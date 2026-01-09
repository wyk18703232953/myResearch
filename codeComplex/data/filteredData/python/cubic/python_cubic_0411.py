import os
import sys
from io import BytesIO, IOBase


def run_algorithm(n, m, k, A, B):
    if k % 2 == 0:
        DP = [[[10**9 for _ in range(m)] for _ in range(n)] for _ in range(k // 2)]
        for i in range(n):
            L = A[i]
            for j in range(m - 1):
                if L[j] < DP[0][i][j]:
                    DP[0][i][j] = L[j]
                if L[j] < DP[0][i][j + 1]:
                    DP[0][i][j + 1] = L[j]

        for i in range(n - 1):
            L = B[i]
            for j in range(m):
                if L[j] < DP[0][i][j]:
                    DP[0][i][j] = L[j]
                if L[j] < DP[0][i + 1][j]:
                    DP[0][i + 1][j] = L[j]

        for k1 in range(1, k // 2):
            for i in range(n):
                for j in range(m):
                    if i > 0:
                        val = B[i - 1][j] + DP[k1 - 1][i - 1][j]
                        if val < DP[k1][i][j]:
                            DP[k1][i][j] = val
                    if j > 0:
                        val = A[i][j - 1] + DP[k1 - 1][i][j - 1]
                        if val < DP[k1][i][j]:
                            DP[k1][i][j] = val
                    if i < n - 1:
                        val = B[i][j] + DP[k1 - 1][i + 1][j]
                        if val < DP[k1][i][j]:
                            DP[k1][i][j] = val
                    if j < m - 1:
                        val = A[i][j] + DP[k1 - 1][i][j + 1]
                        if val < DP[k1][i][j]:
                            DP[k1][i][j] = val

        result_lines = []
        for val in DP[(k // 2) - 1]:
            ans = [x * 2 for x in val]
            result_lines.append(" ".join(str(x) for x in ans))
        return "\n".join(result_lines)

    else:
        result_lines = []
        for _ in range(n):
            ans = [-1] * m
            result_lines.append(" ".join(str(x) for x in ans))
        return "\n".join(result_lines)


def generate_data(n):
    # n controls the grid size; keep k tied to n for scaling
    if n < 1:
        n = 1
    rows = n
    cols = n
    k = 2 * n  # always even so both branches can be tested by changing k if needed

    A = []
    for i in range(rows):
        row = [i * cols + j + 1 for j in range(cols - 1)]
        A.append(row)

    B = []
    for i in range(rows - 1):
        row = [(i + 1) * cols + j + 1 for j in range(cols)]
        B.append(row)

    return rows, cols, k, A, B


def main(n):
    n_rows, n_cols, k, A, B = generate_data(n)
    output = run_algorithm(n_rows, n_cols, k, A, B)
    # print(output)
    pass


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2)
            self.buffer.write(b)
            self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2)
            self.buffer.write(b)
            self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0)
            self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


# endregion

if __name__ == "__main__":
    main(5)