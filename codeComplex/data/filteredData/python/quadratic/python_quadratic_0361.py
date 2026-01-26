import sys
from math import *

def main(n):
    # Interpret n as both rows and columns for a square grid
    if n <= 0:
        # print(0)
        pass
        return
    rows = n
    cols = n

    # Deterministic pattern generation for the grid a:
    # Use a simple arithmetic rule so layout is fixed for given n.
    a = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # Example deterministic rule:
            # Place '*' when (i*j + i + j) % 7 < 3, else '.'
            if (i * j + i + j) % 7 < 3:
                row.append('*')

            else:
                row.append('.')
        a.append(row)

    res = []
    n_rows = rows
    m_cols = cols

    l = [None] * n_rows
    r = [None] * n_rows
    s = [0] * n_rows

    for i in range(n_rows):
        l[i] = [k for k in range(m_cols)]
        r[i] = [k for k in range(m_cols)]
        s[i] = [0] * m_cols

    # Horizontal segment processing
    for i in range(n_rows):
        j = 0
        b = a[i]
        ll = l[i]
        rr = r[i]
        while j < m_cols:
            if b[j] == '*':
                jj = j + 1
                while jj < m_cols and b[jj] == '*':
                    jj += 1
                jj -= 1
                for k in range(j, jj + 1):
                    ll[k] = j
                    rr[k] = jj
                j = jj + 1

            else:
                j += 1

    # Vertical segment processing and center detection
    for i in range(m_cols):
        j = 0
        while j < n_rows:
            if a[j][i] == '*':
                jj = j + 1
                while jj < n_rows and a[jj][i] == '*':
                    jj += 1
                jj -= 1
                for k in range(j, jj + 1):
                    x = min(i - l[k][i], r[k][i] - i, k - j, jj - k)
                    s[k][i] = x
                    if x > 0:
                        res.append((k + 1, i + 1, x))
                j = jj + 1

            else:
                j += 1

    # Build horizontal reconstruction
    for i in range(n_rows):
        j = 0
        ss = s[i]
        rr = r[i]
        c = -1
        while j < m_cols:
            if ss[j] > 0 and c < ss[j]:
                c = ss[j]
            if c >= 0:
                rr[j] = '*'

            else:
                rr[j] = '.'
            j += 1
            c -= 1
        j = m_cols - 1
        c = -1
        while j >= 0:
            if ss[j] > 0 and c < ss[j]:
                c = ss[j]
            if c >= 0:
                rr[j] = '*'
            c -= 1
            j -= 1

    # Build vertical reconstruction and validate
    for i in range(m_cols):
        j = 0
        c = -1
        while j < n_rows:
            x = s[j][i]
            if x > 0 and c < x:
                c = x
            if c >= 0:
                r[j][i] = '*'
            j += 1
            c -= 1
        j = n_rows - 1
        c = -1
        while j >= 0:
            x = s[j][i]
            if x > 0 and c < x:
                c = x
            if c >= 0:
                r[j][i] = '*'
            if r[j][i] != a[j][i]:
                # print(-1)
                pass
                return
            c -= 1
            j -= 1

    # print(len(res))
    pass
    for item in res:
        # print(*item)
        pass
if __name__ == "__main__":
    # Example deterministic call; change the n below for different scales
    main(10)