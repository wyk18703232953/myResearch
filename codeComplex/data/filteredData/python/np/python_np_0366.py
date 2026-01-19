def main(n):
    # n: matrix size (n x n), t is fixed to 1
    if n <= 0:
        return

    # generate deterministic n x n matrix A using simple arithmetic
    # A[i][j] = (i + 1) * (j + 2)
    A = [[(i + 1) * (j + 2) for j in range(n)] for i in range(n)]
    m = n

    # original code logic adapted to use local n
    def maxsa(B, size):
        ans = 0
        for i in range(size):
            cur_maxx = 0
            for j in range(4):
                cur_maxx = max(cur_maxx, B[j][i])
            ans += cur_maxx
        return ans

    def fu(B, size):
        answer = 0
        # make a working copy so rotations don't leak back
        A_local = [row[:] for row in B]
        for _j in range(size):
            A_local[0] = A_local[0][1:] + A_local[0][:1]
            row0 = A_local[0]
            for _i in range(size):
                A_local[1] = A_local[1][1:] + A_local[1][:1]
                row1 = A_local[1]
                for _k in range(size):
                    A_local[2] = A_local[2][1:] + A_local[2][:1]
                    row2 = A_local[2]
                    for _l in range(size):
                        A_local[3] = A_local[3][1:] + A_local[3][:1]
                        # compute max for this rotation
                        cur_ans = maxsa(A_local, size)
                        if cur_ans > answer:
                            answer = cur_ans
                    A_local[3] = row2[:]  # restore before next k-rotation
                A_local[2] = row1[:]      # restore before next i-rotation
            A_local[1] = row0[:]          # restore before next j-rotation
        return answer

    # emulate the body of the for j in range(t) loop with t == 1
    inds = [-1, -1, -1, -1]
    maxs = [0, 0, 0, 0]

    for j in range(m):
        cur_maxs = 0
        for i in range(n):
            cur_maxs = max(cur_maxs, A[i][j])
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
    # example deterministic runs for different scales
    main(3)
    main(5)