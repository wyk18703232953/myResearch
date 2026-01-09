from copy import deepcopy

def sol(n, m, k, aa, bb):
    if k & 1:
        return [[-1] * m for _ in range(n)]
    ans = [[float('inf')] * (m + 2) for _ in range(n + 2)]
    k >>= 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            ans[i][j] = min(aa[i][j], aa[i][j - 1], bb[i][j], bb[i - 1][j])
    for _ in range(k - 1):
        oans = deepcopy(ans)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                ans[i][j] = min(
                    aa[i][j] + oans[i][j + 1],
                    aa[i][j - 1] + oans[i][j - 1],
                    bb[i][j] + oans[i + 1][j],
                    bb[i - 1][j] + oans[i - 1][j]
                )
    ans = ans[1:-1]
    ans = [x[1:-1] for x in ans]
    ans = [[2 * x for x in a] for a in ans]
    return ans

def generate_data(n):
    if n < 2:
        n = 2
    m = n
    k = 2 * ((n % 5) + 1)
    aa = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(i * m + j + 1)
        aa.append(row)
    bb = []
    for i in range(n - 1):
        row = []
        for j in range(m):
            row.append((i + j + 1) * 2)
        bb.append(row)
    inf = float('inf')
    aa = [[inf, *x, inf] for x in aa]
    bb = [[inf, *x, inf] for x in bb]
    pad_aa = [inf] * (m + 2)
    aa = [pad_aa, *aa, pad_aa]
    pad_bb = [inf] * (m + 2)
    bb = [pad_bb, *bb, pad_bb]
    return n, m, k, aa, bb

def main(n):
    n, m, k, aa, bb = generate_data(n)
    ans = sol(n, m, k, aa, bb)
    for row in ans:
        # print(" ".join(map(str, row)))
        pass
if __name__ == "__main__":
    main(5)