def main(n):
    # Map n to grid size. For scalability, use n x n grid.
    # Ensure minimum size 3x3 for the algorithm to have an inner area.
    if n < 3:
        n = 3
    m = n

    # Deterministic generation of S: pattern of '*' and '.'
    # Example: star if (i+j) % 3 != 0 else dot
    S = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i + j) % 3 == 0:
                row.append('.')

            else:
                row.append('*')
        S.append(row)

    L = [[0]*m for _ in range(n)]
    R = [[0]*m for _ in range(n)]
    U = [[0]*m for _ in range(n)]
    D = [[0]*m for _ in range(n)]

    for i in range(n):
        cnt = 0
        for j in range(m):
            if S[i][j] == '.':
                cnt = 0

            else:
                cnt += 1
                L[i][j] = cnt
        cnt = 0
        for j in reversed(range(m)):
            if S[i][j] == '.':
                cnt = 0

            else:
                cnt += 1
                R[i][j] = cnt

    for j in range(m):
        cnt = 0
        for i in range(n):
            if S[i][j] == '.':
                cnt = 0

            else:
                cnt += 1
                U[i][j] = cnt
        cnt = 0
        for i in reversed(range(n)):
            if S[i][j] == '.':
                cnt = 0

            else:
                cnt += 1
                D[i][j] = cnt

    imosH = [[0]*(m+1) for _ in range(n)]
    imosV = [[0]*m for _ in range(n+1)]
    ans = []
    for i in range(1, n-1):
        for j in range(1, m-1):
            if S[i][j] == '.':
                continue
            l = L[i][j]-1
            r = R[i][j]-1
            u = U[i][j]-1
            d = D[i][j]-1
            s = min(l, r, u, d)
            if s == 0:
                continue
            ans.append((i+1, j+1, s))
            imosV[i-s][j] += 1
            imosV[i+s+1][j] -= 1
            imosH[i][j-s] += 1
            imosH[i][j+s+1] -= 1

    from itertools import accumulate
    for i in range(n):
        imosH[i] = list(accumulate(imosH[i]))
    for j in range(m):
        for i in range(1, n+1):
            imosV[i][j] += imosV[i-1][j]

    for i in range(n):
        for j in range(m):
            if S[i][j] == '*':
                if imosH[i][j] <= 0 and imosV[i][j] <= 0:
                    # print(-1)
                    pass
                    return

    else:
        # print(len(ans))
        pass
        for triple in ans:
            # print(*triple)
            pass
if __name__ == "__main__":
    main(10)