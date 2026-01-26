import math
import bisect
from collections import Counter, deque

INF = 250005

def generate_input(n):
    # Map n -> (rows, columns, lesson)
    # Ensure at least 1 row and 1 column
    rows = max(1, n)
    cols = max(1, (n % 10) + 1)
    lesson = max(1, n // 2)

    # Generate a deterministic binary matrix as list of strings
    # s[i][j] = '1' if (i * cols + j) % 3 == 0 else '0'
    lines = []
    for i in range(rows):
        row_chars = []
        for j in range(cols):
            if (i * cols + j) % 3 == 0:
                row_chars.append('1')

            else:
                row_chars.append('0')
        lines.append("".join(row_chars))

    return rows, cols, lesson, lines

def main(n):
    n_rows, m_cols, lesson, lines = generate_input(n)

    dp = [[INF for _ in range(lesson + 2)] for _ in range(n_rows + 1)]
    days = [[] for _ in range(n_rows)]

    for i in range(n_rows):
        s = lines[i]
        for j in range(m_cols):
            if s[j] == "1":
                days[i].append(j + 1)

    m = [[INF for _ in range(lesson + 2)] for _ in range(n_rows + 1)]
    for i in range(n_rows):
        for j in range(lesson + 1):
            if j <= len(days[i]):
                if j == len(days[i]):
                    m[i][j] = 0
                    continue

                else:
                    for k in range(0, j + 1):
                        var = days[i][0 + k]
                        var1 = days[i][-1 * max(1, 1 + (j - k))]
                        m[i][j] = min(m[i][j], var1 - var + 1)

    for i in range(lesson + 1):
        dp[0][i] = m[0][i]

    for i in range(1, n_rows):
        for j in range(lesson + 1):
            for k in range(j + 1):
                dp[i][j] = min(dp[i][j], dp[i - 1][j - k] + m[i][k])

    result = min(dp[n_rows - 1])
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)