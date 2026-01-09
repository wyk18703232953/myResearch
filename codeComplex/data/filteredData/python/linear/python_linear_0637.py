def main(n):
    # Interpret n as the array length
    # Deterministically generate array a of length n:
    # mix of 1's and other integers using simple arithmetic
    a = [(i % 5) + 1 for i in range(n)]

    b = []
    c = []
    e = []
    for i in range(n):
        if a[i] == 1:
            b.append(i)
    for i in range(n):
        if a[i] != 1:
            c.append([a[i], i])
    if not c:
        return ("NO", None)

    ans = len(c)
    for i in range(len(c) - 1):
        e.append((c[i][1], c[i + 1][1]))
        c[i][0] -= 1
        c[i + 1][0] -= 1
    if b:
        e.append((b[-1], c[-1][1]))
        c[-1][0] -= 1
        b.pop()
        ans += 1
    if b:
        e.append((b[-1], c[0][1]))
        c[0][0] -= 1
        b.pop()
        ans += 1
    i = 0
    while b:
        while i < len(c) and c[i][0] == 0:
            i += 1
        if i == len(c):
            return ("NO", None)
        e.append((b[-1], c[i][1]))
        c[i][0] -= 1
        b.pop()

    # Prepare output in the same structure as original program
    result_lines = []
    result_lines.append(f"YES {ans - 1}")
    result_lines.append(str(len(e)))
    for (x, y) in e:
        result_lines.append(f"{x + 1} {y + 1}")
    return ("\n".join(result_lines), (a, e))


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    # You can change this n to scale the input size.
    n = 10
    output, _ = main(n)
    if output is None:
        # print("NO")
        pass

    else:
        # print(output)
        pass