def createDP(R, G, B):
    dp = []
    for i in range(R):
        temp1 = []
        for j in range(G):
            temp2 = []
            for k in range(B):
                temp2.append(-1)
            temp1.append(temp2)
        dp.append(temp1)
    return dp

def go(r, g, b, R, G, B, ri, gi, bi, state):
    if state[ri][gi][bi] != -1:
        return state[ri][gi][bi]
    best = 0
    if ri < R and gi < G:
        best = max(best, r[ri] * g[gi] + go(r, g, b, R, G, B, ri + 1, gi + 1, bi, state))
    if ri < R and bi < B:
        best = max(best, r[ri] * b[bi] + go(r, g, b, R, G, B, ri + 1, gi, bi + 1, state))
    if gi < G and bi < B:
        best = max(best, g[gi] * b[bi] + go(r, g, b, R, G, B, ri, gi + 1, bi + 1, state))
    state[ri][gi][bi] = best
    return best

def main(n):
    if n < 1:
        n = 1
    # 映射规模：三种颜色数组长度相同，均为 n
    R = G = B = n

    # 确定性生成数据：简单递增序列
    r = [i + 1 for i in range(R)]
    g = [2 * (i + 1) for i in range(G)]
    b = [3 * (i + 1) for i in range(B)]

    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    # 原程序中 DP 维度固定为 201，这里也保持不变以保留逻辑结构
    dp = createDP(201, 201, 201)
    result = go(r, g, b, R, G, B, 0, 0, 0, dp)
    # print(result)
    pass
if __name__ == "__main__":
    main(5)