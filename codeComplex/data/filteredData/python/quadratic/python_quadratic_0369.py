def main(n):
    # Map n to grid size h x w
    # Use h = w = n for scalability
    h = n
    w = n

    # Deterministically generate a pattern of '*' and '.'
    # Example rule: cell (i,j) is '*' if (i*j) % 7 == 0 and (i+j) % 3 != 0
    # i,j are 1-based for consistency with original code logic
    s = [list("." * (w + 2))]
    for i in range(1, h + 1):
        row = ["."]
        for j in range(1, w + 1):
            if (i * j) % 7 == 0 and (i + j) % 3 != 0:
                row.append("*")

            else:
                row.append(".")
        row.append(".")
        s.append(row)
    s.append(list("." * (w + 2)))

    b = [[0] * (w + 2) for _ in range(h + 2)]
    c = [[0] * (w + 2) for _ in range(h + 2)]

    for i in range(1, h + 2):
        for j in range(1, w + 2):
            if s[i][j] == "*":
                b[i][j] = b[i - 1][j] + 1
                c[i][j] = c[i][j - 1] + 1

    for i in range(h, -1, -1):
        for j in range(w, -1, -1):
            if s[i][j] == "*":
                b[i][j] = min(b[i][j], b[i + 1][j] + 1)
                c[i][j] = min(c[i][j], c[i][j + 1] + 1)

    ans = []
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            t = min(b[i][j], c[i][j]) - 1
            if t > 0:
                ans.append((i, j, t))

    b = [[0] * (w + 2) for _ in range(h + 2)]
    c = [[0] * (w + 2) for _ in range(h + 2)]

    for i, j, t in ans:
        b[i - t][j] += 1
        b[i + t + 1][j] -= 1
        c[i][j - t] += 1
        c[i][j + t + 1] -= 1

    valid = True
    for i in range(h + 1):
        for j in range(w + 1):
            b[i + 1][j] += b[i][j]
            c[i][j + 1] += c[i][j]
            if i != 0 and j != 0:
                if (b[i][j] + c[i][j] > 0) != (s[i][j] == "*"):
                    valid = False

    # For determinism, still output something even if invalid.
    # Original code would print -1 and exit; here we mimic it in the return/output.
    if not valid:
        # print(-1)
        pass
        return

    # print(len(ans))
    pass
    for item in ans:
        # print(*item)
        pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(300)