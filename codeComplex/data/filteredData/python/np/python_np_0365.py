def main(n):
    # n is both number of rows and columns of the matrix A in the original problem
    # We also treat t (number of test cases) as n, to scale work linearly with n
    if n <= 0:
        return

    def maxsa(A, n_local):
        ans = 0
        for i in range(n_local):
            cur_maxx = 0
            for j in range(4):
                cur_maxx = max(cur_maxx, A[j][i])
            ans += cur_maxx
        return ans

    def fu(A, n_local):
        answer = 0
        # The original fu rotates rows many times; this is O(n^4 * n) behavior.
        # We keep the same structure but operate on local copies.
        row0 = A[0][:]
        row1 = A[1][:]
        row2 = A[2][:]
        row3 = A[3][:]
        for _ in range(n_local):
            row0 = row0[1:] + row0[:1]
            for _ in range(n_local):
                row1 = row1[1:] + row1[:1]
                for _ in range(n_local):
                    row2 = row2[1:] + row2[:1]
                    for _ in range(n_local):
                        row3 = row3[1:] + row3[:1]
                        cur_A = [row0, row1, row2, row3]
                        cur_ans = maxsa(cur_A, n_local)
                        if cur_ans > answer:
                            answer = cur_ans
        return answer

    # Deterministic generation of t test cases
    t = n
    for case_idx in range(t):
        # Deterministic m in [1, n], but at least 1 and at most n
        m = n if n > 0 else 1

        # Generate A as n x m matrix, entries depend on case_idx, row, col
        A = []
        for i in range(n):
            row = []
            for j in range(m):
                val = (case_idx + 1) * (i + 1) + (j + 1)
                row.append(val)
            A.append(row)

        # Original logic selecting up to 4 best columns by column-wise max
        inds = [-1, -1, -1, -1]
        maxs = [0, 0, 0, 0]
        for j in range(m):
            cur_maxs = 0
            for i in range(n):
                if A[i][j] > cur_maxs:
                    cur_maxs = A[i][j]
            maxs.append(cur_maxs)
            inds.append(j)
            ind = 4
            while ind != 0 and maxs[ind] > maxs[ind - 1]:
                inds[ind], inds[ind - 1] = inds[ind - 1], inds[ind]
                maxs[ind], maxs[ind - 1] = maxs[ind - 1], maxs[ind]
                ind -= 1
            maxs.pop()
            inds.pop()

        S = [0] * 4
        for j in range(4):
            if inds[j] != -1:
                S[j] = [row[inds[j]] for row in A]
            else:
                S[j] = [0] * n

        result = fu(S, n)
        print(result)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)