# from math import ceil
#
#
# n, k = map(int, input().split())
# lst = [0] * k
# sets = ceil(n/2)
# stud = 0
# for i in range(n):
#     temp = int(input())
#     if sets == 0:
#         continue
#     for i in range(1, k+1):
#         if temp ==  i:
#             if lst[i-1] == 0:
#                 lst[i-1] += 1
#             else:
#                 sets -= 1
#                 lst[i-1] = 0
#                 stud += 2
# if sets == 0:
#     print(stud)
# else:
#     print(stud + sets)
from math import sqrt
n, k = map(int, input().split())
a = 1
b = -1 * (2*n + 3)
c = n * (n + 1) - 2 * k

res = (-1 * b) - sqrt((b * b) - 4 * a * c)
res = res / 2
res = int(res)
print(res)
