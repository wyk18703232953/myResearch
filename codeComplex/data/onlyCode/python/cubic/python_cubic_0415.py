from heapq import heappop, heappush

n, m, k = [int(i) for i in input().split()]
if k % 2 == 1:
    for _ in range(n):
        print(" ".join(["-1"] * m))
    exit()

E_right = []
for i in range(n):
    E_right.append([int(j) for j in input().split()])

E_down = []
for i in range(n - 1):
    E_down.append([int(j) for j in input().split()])

P = [[0 for _ in range(m)] for _ in range(n)]
new_P = [[0 for _ in range(m)] for _ in range(n)]

for k in range(k // 2 + 1):
    for i in range(n):
        for j in range(m):
            possible = []
            if i - 1 >= 0:
                e = E_down[i - 1][j]
                possible.append(P[i - 1][j] + e)

            if i + 1 < n:
                e = E_down[i][j]
                possible.append(P[i + 1][j] + e)

            if j - 1 >= 0:
                e = E_right[i][j - 1]
                possible.append(P[i][j - 1] + e)
            
            if j + 1 < m:
                e = E_right[i][j]
                possible.append(P[i][j + 1] + e)

            new_P[i][j] = min(possible)

    tmp = P
    P = new_P
    new_P = tmp

for i in range(n):
    print(" ".join(str(s * 2) for s in new_P[i]))

            


            

# for i in range(n):
#     ans = []
#     for j in range(m):
#         nodes = [(0, 0, i, j)]

#         while True:
#             l, kk, n_i, n_j = heappop(nodes)
#             if kk == k // 2:
#                 ans.append(l * 2)
#                 break

#             if n_i - 1 >= 0:
#                 e = E_down[n_i - 1][n_j]
#                 heappush(nodes, (l + e, kk + 1, n_i - 1, n_j))

#             if n_i + 1 < n:
#                 e = E_down[n_i][n_j]
#                 heappush(nodes, (l + e, kk + 1, n_i + 1, n_j))

#             if n_j - 1 >= 0:
#                 e = E_right[n_i][n_j - 1]
#                 heappush(nodes, (l + e, kk + 1, n_i, n_j - 1))
            
#             if n_j + 1 < m:
#                 e = E_right[n_i][n_j]
#                 heappush(nodes, (l + e, kk + 1, n_i, n_j + 1))

#     print(" ".join(str(l) for l in ans))




    
     

    