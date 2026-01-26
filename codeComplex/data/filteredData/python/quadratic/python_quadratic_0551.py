import sys

def main(n):
    # Interpret n as the grid size n x n
    if n <= 0:
        return
    m = n
    ans = []
    moves = n * m
    c1 = [1, 1]
    c2 = [n, m]
    p = 0
    while moves > 0:
        if p % 2 == 0:
            ans.append((c1[0], c1[1]))
            c1[1] += 1
            if c1[1] > m:
                c1[0] += 1
                c1[1] = 1

        else:
            ans.append((c2[0], c2[1]))
            c2[1] -= 1
            if c2[1] < 1:
                c2[0] -= 1
                c2[1] = m
        moves -= 1
        p += 1

    out_lines = []
    for i in ans:
        out_lines.append(f"{i[0]} {i[1]}")
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(5)