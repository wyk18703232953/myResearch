def main(n):
    # Map n to grid size n x n
    if n < 3:
        n = 3
    m = n

    # Deterministic generation of original grid s
    # Pattern: '#' where (i + j) is divisible by 3, else '.'
    s = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i + j) % 3 == 0:
                row.append('#')
            else:
                row.append('.')
        s.append(row)

    # Initialize t with '.'
    t = []
    for i in range(n):
        p = ['.'] * m
        t.append(p)

    # Core algorithm (unchanged logic)
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            f = 0
            if (
                s[i - 1][j - 1] == '#' and
                s[i - 1][j] == '#' and
                s[i - 1][j + 1] == '#' and
                s[i][j - 1] == '#' and
                s[i][j + 1] == '#' and
                s[i + 1][j - 1] == '#' and
                s[i + 1][j] == '#' and
                s[i + 1][j + 1] == '#'
            ):
                f = 1
            if f == 1:
                t[i - 1][j - 1] = '#'
                t[i - 1][j] = '#'
                t[i - 1][j + 1] = '#'
                t[i][j - 1] = '#'
                t[i][j + 1] = '#'
                t[i + 1][j - 1] = '#'
                t[i + 1][j] = '#'
                t[i + 1][j + 1] = '#'

    f = 1
    for i in range(n):
        for j in range(m):
            if s[i][j] == '#' and s[i][j] != t[i][j]:
                f = 0
                break
        if f == 0:
            break

    if f == 1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)