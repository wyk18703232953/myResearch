import sys

def generate_input(n):
    if n < 2:
        n = 2
    # map n to grid size; keep it square-ish
    rows = n
    cols = n
    k = 2 * n  # even, scales with n

    # construct input sequence as original code expects
    data = [rows, cols, k]

    # yw: n rows, each m-1 integers
    # deterministic weights using simple arithmetic
    for i in range(rows):
        for j in range(cols - 1):
            data.append((i + 1) * (j + 2))

    # xw: n-1 rows, each m integers
    for i in range(rows - 1):
        for j in range(cols):
            data.append((i + 2) * (j + 1))

    return data

def run_algorithm(inp):
    ii = 0

    n = inp[ii]; ii += 1
    m = inp[ii]; ii += 1
    k = inp[ii]; ii += 1

    if k % 2 == 1:
        result = []
        for _ in range(n):
            toprint = ["-1" for __ in range(m)]
            result.append(" ".join(toprint))
        return "\n".join(result)

    yw = []
    for _ in range(n):
        yw.append(inp[ii:ii + m - 1])
        ii += m - 1

    xw = []
    for _ in range(n - 1):
        xw.append(inp[ii:ii + m])
        ii += m

    inf = 10 ** 10
    steps = k // 2

    dp = [[[inf for _ in range(m)] for _ in range(n)] for _ in range(steps + 1)]

    for i in range(n):
        for j in range(m):
            dp[0][i][j] = 0

    for step in range(1, steps + 1):
        for i in range(n):
            for j in range(m):
                if i > 0:
                    dp[step][i][j] = min(dp[step][i][j], dp[step - 1][i - 1][j] + xw[i - 1][j])
                if i < n - 1:
                    dp[step][i][j] = min(dp[step][i][j], dp[step - 1][i + 1][j] + xw[i][j])
                if j > 0:
                    dp[step][i][j] = min(dp[step][i][j], dp[step - 1][i][j - 1] + yw[i][j - 1])
                if j < m - 1:
                    dp[step][i][j] = min(dp[step][i][j], dp[step - 1][i][j + 1] + yw[i][j])

    lines = []
    for row in dp[-1]:
        lines.append(" ".join(str(2 * o) for o in row))
    return "\n".join(lines)

def main(n):
    inp = generate_input(n)
    output = run_algorithm(inp)
    # print(output)
    pass
if __name__ == "__main__":
    main(5)