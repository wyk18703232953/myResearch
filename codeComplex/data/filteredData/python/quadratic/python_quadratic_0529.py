def main(n):
    # n controls the grid size: R = C = max(3, n)
    R = max(3, n)
    C = max(3, n)

    # Deterministic grid generation:
    # Place '#' where (r*c) % 3 == 0, else '.'
    m = []
    count = 0
    for r in range(R):
        row_chars = []
        for c in range(C):
            if (r * c) % 3 == 0:
                row_chars.append('#')
                count += 1
            else:
                row_chars.append('.')
        m.append(''.join(row_chars))

    D = False

    def hash_cell(r, c):
        return str(r) + "-" + str(c)

    lookup = {}
    for r in range(1, R - 1):
        for c in range(1, C - 1):

            if D:
                print("  row,col:", r, c)

            offset = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
            lst = []
            fail = False

            # ensure all 8 adj cells are '#'
            for o in offset:
                cell = (r + o[0], c + o[1])
                if D:
                    print("  cell:", cell, m[cell[0]][cell[1]])
                h = hash_cell(cell[0], cell[1])

                if m[cell[0]][cell[1]] == "#":
                    if h not in lookup:
                        lst.append(h)
                else:
                    fail = True
                    break

            if not fail:
                for item in lst:
                    lookup[item] = True
                count -= len(lst)

    return "YES" if count == 0 else "NO"


if __name__ == "__main__":
    # example call for complexity experiments
    print(main(10))