def getArray():
    return list(map(int, input().split()))
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
    if state[ri][gi][bi] != -1 :
        return state[ri][gi][bi]
    best = 0
    if ri < R and gi < G:
        best = max(best, r[ri]*g[gi] + go(r, g, b, R, G, B, ri+1, gi+1, bi, state))
    if ri < R and bi < B:
        best = max(best, r[ri]*b[bi] + go(r, g, b, R, G, B, ri+1, gi, bi+1, state))
    if gi < G and bi < B:
        best = max(best, g[gi]*b[bi] + go(r, g, b, R, G, B, ri, gi+1, bi+1, state))
    
    state[ri][gi][bi] = best
    return best
    
R,G,B = map(int, input().split())
r = getArray()
g = getArray()
b = getArray()
r.sort(reverse = True)
g.sort(reverse = True)
b.sort(reverse = True)
dp = createDP(201,201,201)
print(go(r, g, b, R, G, B, 0, 0, 0, dp))