from math import inf


n = int(input())
s_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

total_min = inf
for j in range(n):
    min_i = inf
    for i in range(0, j):
        if s_list[i] < s_list[j]:
            min_i = min(min_i, c_list[i])

    min_k = inf
    for k in range(j + 1, n):
        if s_list[k] > s_list[j]:
            min_k = min(min_k, c_list[k])

    total_min = min(total_min, min_i + c_list[j] + min_k)
if total_min != inf:
    print(total_min)
else:
    print(-1)