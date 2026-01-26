def solveBFS(NR, NG, NB, R, G, B):
    from collections import deque

    def pack(i, j, k):
        return i * 256 * 256 + j * 256 + k

    def unpack(ijk):
        i, jk = divmod(ijk, 256 * 256)
        j, k = divmod(jk, 256)
        return i, j, k

    R.sort(reverse=True)
    G.sort(reverse=True)
    B.sort(reverse=True)
    dp = [0 for _ in range(256 ** 3)]
    q = deque([0])
    while q:
        ijk = q.popleft()
        d = dp[ijk]
        i, j, k = unpack(ijk)

        if i < NR:
            r = R[i]
        if j < NG:
            g = G[j]
        if k < NB:
            b = B[k]

        if i + 1 <= NR and j + 1 <= NG:
            rg = pack(i + 1, j + 1, k)
            val = r * g + d
            if val > dp[rg]:
                dp[rg] = val
                q.append(rg)

        if i + 1 <= NR and k + 1 <= NB:
            rb = pack(i + 1, j, k + 1)
            val = r * b + d
            if val > dp[rb]:
                dp[rb] = val
                q.append(rb)

        if j + 1 <= NG and k + 1 <= NB:
            gb = pack(i, j + 1, k + 1)
            val = g * b + d
            if val > dp[gb]:
                dp[gb] = val
                q.append(gb)

    return max(dp)


def solve(NR, NG, NB, R, G, B):
    assert NR == len(R)
    R.sort(reverse=True)
    G.sort(reverse=True)
    B.sort(reverse=True)

    R += [0]
    G += [0]
    B += [0]

    NR1 = NR + 2
    NG1 = NG + 2
    NB1 = NB + 2
    dp = [0 for _ in range(NR1 * NG1 * NB1)]

    def pack(i, j, k):
        return i * NG1 * NB1 + j * NB1 + k

    inf = float("inf")
    for i in range(NR + 1):
        for j in range(NG + 1):
            dp[pack(i, j, -1)] = -inf
    for i in range(NR + 1):
        for k in range(NB + 1):
            dp[pack(i, -1, k)] = -inf
    for j in range(NG + 1):
        for k in range(NB + 1):
            dp[pack(-1, j, k)] = -inf

    for l in range(2, NR + NG + NB + 1, 2):
        for j in range(NG + 1):
            for k in range(NB + 1):
                i = l - j - k
                if i < 0 or i > NR:
                    continue
                r = R[i - 1]
                g = G[j - 1]
                b = B[k - 1]
                dp[pack(i, j, k)] = max(
                    r * g + dp[pack(i - 1, j - 1, k)],
                    r * b + dp[pack(i - 1, j, k - 1)],
                    b * g + dp[pack(i, j - 1, k - 1)],
                )

    return max(dp)


def main(n):
    # 定义输入规模：三个数组的长度都为 n
    NR = NG = NB = n

    # 确定性生成测试数据
    # R, G, B 的元素大小与索引相关，避免随机性
    R = [(i % 7) + 1 for i in range(NR)]
    G = [(i % 11) + 1 for i in range(NG)]
    B = [(i % 13) + 1 for i in range(NB)]

    ans = solve(NR, NG, NB, R, G, B)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：输入规模 n = 10
    main(10)