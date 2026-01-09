def main(n):
    # Deterministically generate parameters a, b based on n
    a = n % 10 + 1
    b = (n // 10) % 10 + 1  # unused in original logic but kept for structure

    # Generate n lines corresponding to original input structure: (t, x, y)
    # Original code ignores the first element of each tuple, so set it deterministically as i
    data = []
    for i in range(n):
        x = (i * a + b) % (2 * n + 1)
        y = (i * b + a) % (2 * n + 1)
        data.append((i, x, y))

    c, d = {}, {}
    r = 0
    for _, x, y in data:
        i_val = a * x - y
        j_val = (x, y)
        r += c.get(i_val, 0) - d.get(j_val, 0)
        c[i_val] = c.get(i_val, 0) + 1
        d[j_val] = d.get(j_val, 0) + 1
    # print(2 * r)
    pass
if __name__ == "__main__":
    # Example: run with n = 1000
    main(1000)