def main(n):
    # Interpret n as both number of test cases and base matrix size
    t = n if n > 0 else 1

    for case_id in range(t):
        # For each test case, define dimensions deterministically from n and case_id
        # Ensure n_rows, n_cols >= 1
        n_rows = (n + case_id) % max(1, n) + 1
        n_cols = (2 * n + case_id) % max(1, n) + 1

        # Build board deterministically; size: n_rows x n_cols
        board = []
        l = []
        for i in range(n_rows):
            row = []
            for j in range(n_cols):
                # Deterministic value depending on n, case_id, i, j
                val = (n + 1) * (case_id + 1) + i * n_cols + j
                row.append(val)
                l.append((val, j))
            board.append(row)

        # Keep original logic
        l.sort(key=lambda x: x[0], reverse=True)
        idxs = set()
        z = 0
        while len(idxs) < min(n_rows, n_cols):
            curr = l[z]
            idxs.add(curr[1])
            z += 1
        idxs = list(idxs)
        total = 0
        for i in range(n_rows ** n_rows):
            rotations = []
            num = i
            for j in range(n_rows - 1, -1, -1):
                nj = n_rows ** j
                q = num // nj
                num -= q * nj
                rotations.append(q)
            subtotal = 0
            for k in range(n_rows):
                subtotal += max(
                    board[(k + rotations[col]) % n_rows][idxs[col]]
                    for col in range(min(n_rows, n_cols))
                )
            total = max(total, subtotal)
        print(total)


if __name__ == "__main__":
    main(3)