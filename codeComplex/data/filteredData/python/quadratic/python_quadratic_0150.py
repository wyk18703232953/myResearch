def main(n):
    # Generate four n x n binary boards as lists of "strings in a list" (matching input structure)
    # Each row is like ["0101..."] so that lst[x][0][y] indexing stays the same.
    def generate_board(offset):
        rows = []
        for i in range(n):
            row_chars = []
            for j in range(n):
                # deterministic pattern depending on i, j, offset
                val = (i * n + j + offset) % 2
                row_chars.append(str(val))
            rows.append(["".join(row_chars)])
        return rows

    lst1 = generate_board(0)
    s = "ignored"
    lst2 = generate_board(1)
    s = "ignored"
    lst3 = generate_board(2)
    s = "ignored"
    lst4 = generate_board(3)

    ans_b1 = 0
    ans_w1 = 0
    for x in range(n):
        for y in range(n):
            if (x + y) & 1 == 0:
                if lst1[x][0][y] == '0':
                    ans_b1 += 1
                else:
                    ans_w1 += 1
            else:
                if lst1[x][0][y] == '1':
                    ans_b1 += 1
                else:
                    ans_w1 += 1

    ans_b2 = 0
    ans_w2 = 0
    for x in range(n):
        for y in range(n):
            if (x + y) & 1 == 0:
                if lst2[x][0][y] == '0':
                    ans_b2 += 1
                else:
                    ans_w2 += 1
            else:
                if lst2[x][0][y] == '1':
                    ans_b2 += 1
                else:
                    ans_w2 += 1

    ans_b3 = 0
    ans_w3 = 0
    for x in range(n):
        for y in range(n):
            if (x + y) & 1 == 0:
                if lst3[x][0][y] == '0':
                    ans_b3 += 1
                else:
                    ans_w3 += 1
            else:
                if lst3[x][0][y] == '1':
                    ans_b3 += 1
                else:
                    ans_w3 += 1

    ans_b4 = 0
    ans_w4 = 0
    for x in range(n):
        for y in range(n):
            if (x + y) & 1 == 0:
                if lst4[x][0][y] == '0':
                    ans_b4 += 1
                else:
                    ans_w4 += 1
            else:
                if lst4[x][0][y] == '1':
                    ans_b4 += 1
                else:
                    ans_w4 += 1

    result = (2 * n) ** 2 - max(
        ans_b1 + ans_b2 + ans_w3 + ans_w4,
        ans_b1 + ans_w2 + ans_b3 + ans_w4,
        ans_b1 + ans_w2 + ans_w3 + ans_b4,
        ans_w1 + ans_b2 + ans_b3 + ans_w4,
        ans_w1 + ans_b2 + ans_w3 + ans_b4,
        ans_w1 + ans_w2 + ans_b3 + ans_b4,
    )
    print(result)
    return result


if __name__ == "__main__":
    main(4)