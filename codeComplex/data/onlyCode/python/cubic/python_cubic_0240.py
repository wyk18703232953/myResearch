import sys
input = sys.stdin.readline

r, g, b, = [int(_) for _ in input().split()]
R = [int(_) for _ in input().split()]
G = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]
R = sorted(R, reverse=True)
G = sorted(G, reverse=True)
B = sorted(B, reverse=True)

dp = []  # best score so far after picking (iR, jG, kB)
for i in range(r+1):
    sdp = [[0]*(b+1) for _ in range(g+1)]
    dp.append(sdp)

answer = 0
for nb_taken in range(r+g+b):
    if nb_taken % 2:
        continue
    # print('nb_taken', nb_taken)
    for i in range(nb_taken+1):
        if i > r:
            break
        for j in range(nb_taken-i-b, nb_taken-i+1):
            if j > g:
                break
            k = nb_taken-i-j
            if k > b:
                continue
            if i+j < k or i+k < j or j+k < i:
                continue
            # assert i+j+k == nb_taken
            # print('in dp', i, j, k)
# for i in range(r):
    # for j in range(g):
        # for k in range(b):
            if i < r and j < g:
                dp[i+1][j+1][k] = max(dp[i+1][j+1][k], dp[i][j][k] + R[i]*G[j])
                # print('setting dp', i+1, j+1, k, dp[i+1][j+1][k])
                answer = max(answer, dp[i+1][j+1][k])
            if i < r and k < b:
                dp[i+1][j][k+1] = max(dp[i+1][j][k+1], dp[i][j][k] + R[i]*B[k])
                # print('setting dp', i+1, j, k+1, dp[i+1][j][k+1])
                answer = max(answer, dp[i+1][j][k+1])
            if j < g and k < b:
                dp[i][j+1][k+1] = max(dp[i][j+1][k+1], dp[i][j][k] + G[j]*B[k])
                # print('setting dp', i, j+1, k+1, dp[i][j+1][k+1])
                answer = max(answer, dp[i][j+1][k+1])
# print(dp)
print(answer)

# k > b <=> nb_taken-i-j >= b <=> j <= nb_taken-i-b
