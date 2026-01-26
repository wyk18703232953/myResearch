def main():
    N, M, K = map(int, input().split())

    if K % 2:
        print(("-1 " * M + "\n") * N)
        return

    colEdges = []
    for i in range(N):
        edges = list(map(int, input().split()))
        colEdges.append(edges)
    
    rowEdges = []
    for i in range(N - 1):
        edges = list(map(int, input().split()))
        rowEdges.append(edges)
    
    dp = [[[0 for i in range(M)] for j in range(N)] for k in range(2)]
    p = [[[(i, j) for j in range(M)] for i in range(N)] for k in range(2)]
    prev = 0
    for k in range(K // 2):
        cur = prev ^ 1
        for i in range(N):
            for j in range(M):
                cand = (float('inf'), None)

                if j:
                    nxt = (dp[prev][i][j - 1] + colEdges[i][j - 1], p[prev][i][j - 1])
                    cand = min(cand, nxt)
                if j < M - 1:
                    nxt = (dp[prev][i][j + 1] + colEdges[i][j], p[prev][i][j + 1])
                    cand = min(cand, nxt)
                if i:
                    nxt = (dp[prev][i - 1][j] + rowEdges[i - 1][j], p[prev][i - 1][j])
                    cand = min(cand, nxt)
                if i < N - 1:
                    nxt = (dp[prev][i + 1][j] + rowEdges[i][j], p[prev][i + 1][j])
                    cand = min(cand, nxt)
                
                dp[cur][i][j], p[cur][i][j] = cand
        prev = cur
    
    for i in range(N):
        for j in range(M):
             print(dp[prev][i][j] * 2, end=" ")
        print()
main()