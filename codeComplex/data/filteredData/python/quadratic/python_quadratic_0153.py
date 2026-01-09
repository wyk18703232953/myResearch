def main(n):
    def rd(row_index):
        # deterministic generation of a row of length n
        # original rd() consumes digits from input(); here we generate 0/1 based on i and row_index
        return [(i + row_index) & 1 for i in range(n)]

    def f(n, t):
        a = 0
        for i in range(n):
            row = rd(i + t * n)
            for j, x in enumerate(row):
                if ((i + j) & 1) == x:
                    a += 1
        if t < 3:
            # consume another n positions deterministically to simulate rd() call
            _ = rd((t + 4) * n)
        return a

    m = sorted([f(n, i) for i in range(4)])
    result = 2 * n * n + m[0] + m[1] - m[2] - m[3]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)