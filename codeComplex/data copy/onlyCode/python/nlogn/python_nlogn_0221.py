n, U = list(map(int, input().split()))
E = list(map(int, input().split()))

ind_i = 0
prev_ind_k = ind_i + 2

maxi_efficiency = -1
turn = 0
for ind_i in range(0, n - 2):
    ind_j = ind_i + 1
    prev_ind_k = max(prev_ind_k, ind_i + 2)
    Ei = E[ind_i]
    Ej = E[ind_j]
    for ind_k in range(prev_ind_k, n + 1):
        # print("ind_i, ind_k", ind_i, ind_k)
        if ind_k == n:
            prev_ind_k = n - 1
            break
        Ek = E[ind_k]
        if (Ek - Ei) > U:
            prev_ind_k = ind_k - 1
            break

        efficiency = (Ek - Ej) / (Ek - Ei)
        # print("efficiency : ", efficiency)
        if efficiency > maxi_efficiency:
            # print(ind_i, ind_k)
            maxi_efficiency = efficiency

print(maxi_efficiency)

# if (ind_i == n-3 and ind_j == n-2 and ind_k == n-1):
#     break


# n, U = list(map(int, input().split()))
# E = list(map(int, input().split()))

# ind_i = 0
# ind_k = 2

# maxi_efficiency = -1
# turn = 0
# while ind_i < n - 2 and ind_k < n:
#     # print("ind_i, ind_j : ", ind_i, ind_k)
#     ind_j = ind_i + 1
#     Ei = E[ind_i]
#     Ej = E[ind_j]
#     Ek = E[ind_k]
#     if (Ek - Ei) > U:
#         # print("too much")
#         ind_i += 1
#         ind_k = max(ind_k, ind_i + 2)
#         continue
#     else:
#         efficiency = (Ek - Ej) / (Ek - Ei)
#         # print("efficiency : ", efficiency)
#         if efficiency > maxi_efficiency:
#             print(ind_i, ind_k)
#             maxi_efficiency = efficiency
#         ind_k += 1

# print(maxi_efficiency)

# if (ind_i == n-3 and ind_j == n-2 and ind_k == n-1):
#     break


# n, U = list(map(int, input().split()))
# E = list(map(int, input().split()))

# ind_i = 0

# maxi_efficiency = -1
# turn = 0
# while ind_i < n - 3:
#     ind_j = ind_i + 1
#     Ei = E[ind_i]
#     Ej = E[ind_j]
#     for ind_k in range(ind_j + 1, n):
#         Ek = E[ind_k]
#         if (Ek - Ei) > U:
#             break

#         efficiency = (Ek - Ej) / (Ek - Ei)
#         # print("efficiency : ", efficiency)
#         if efficiency > maxi_efficiency:
#             maxi_efficiency = efficiency

#     ind_i += 1

# print(maxi_efficiency)

# # if (ind_i == n-3 and ind_j == n-2 and ind_k == n-1):
# #     break
