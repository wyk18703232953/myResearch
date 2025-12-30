import random

def createDP(R, G, B):
    dp = []
    for i in range(R + 1):
        temp1 = []
        for j in range(G + 1):
            temp2 = []
            for k in range(B + 1):
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
    # 根据规模 n 生成测试数据
    # 这里令数组长度 R, G, B 均为 n，元素为 1..100 的随机整数
    R = G = B = n
    r = [random.randint(1, 100) for _ in range(R)]
    g = [random.randint(1, 100) for _ in range(G)]
    b = [random.randint(1, 100) for _ in range(B)]

    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    dp = createDP(R, G, B)
    ans = go(r, g, b, R, G, B, 0, 0, 0, dp)
    print(ans)

if __name__ == "__main__":
    # 示例：规模为 3
    main(3)