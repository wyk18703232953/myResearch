def main(n):
    t = n
    results = []
    for i in range(t):
        # Deterministic grid size depending on i and n
        rows = (i + 1) * 2
        cols = (n + i + 1) * 2

        n_rows = rows
        m_cols = cols

        # Deterministically generate first rectangle
        # Ensure valid coordinates: 1-based indexing
        x1 = 1
        y1 = 1
        x2 = max(1, n_rows // 2)
        y2 = max(1, m_cols // 2)

        # Deterministically generate second rectangle, overlapping pattern
        x3 = max(1, n_rows // 3)
        y3 = max(1, m_cols // 3)
        x4 = n_rows
        y4 = m_cols

        n_cells = n_rows * m_cols
        count_w = n_cells // 2 + n_cells % 2
        count_g = n_cells // 2

        rect1_cells = (x2 - x1 + 1) * (y2 - y1 + 1)
        if (x1 + y1) % 2 == 0:
            count_g -= rect1_cells // 2
            count_w += rect1_cells // 2

        else:
            count_g -= rect1_cells // 2 + rect1_cells % 2
            count_w += rect1_cells // 2 + rect1_cells % 2

        x5 = max(x1, x3)
        x6 = min(x4, x2)
        y5 = max(y1, y3)
        y6 = min(y4, y2)

        rect2_cells = (x4 - x3 + 1) * (y4 - y3 + 1)
        if (x3 + y3) % 2 == 1:
            count_g += rect2_cells // 2
            count_w -= rect2_cells // 2

        else:
            count_g += rect2_cells // 2 + rect2_cells % 2
            count_w -= rect2_cells // 2 + rect2_cells % 2

        if x5 <= x6 and y5 <= y6:
            inter_cells = (x6 - x5 + 1) * (y6 - y5 + 1)
            if (x5 + y5) % 2 == 0:
                count_g += inter_cells // 2
                count_w -= inter_cells // 2

            else:
                count_g += inter_cells // 2 + inter_cells % 2
                count_w -= inter_cells // 2 + inter_cells % 2

        results.append((count_w, count_g))

    for cw, cg in results:
        # print(cw, cg)
        pass
if __name__ == "__main__":
    main(10)