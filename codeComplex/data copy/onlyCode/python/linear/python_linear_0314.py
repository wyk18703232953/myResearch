# n, m = map(int, input().split())
#
# arr = [int(z) for z in input().split()]
# modvals = []
#
# for i in range(n):
#     modvals.append([arr[i] % m, i])
#
# modvals.sort()
#
# rem = {}
# used = {}
#
# for i in range(m):
#     rem[i] = 0
#     used[i] = 0
#
# for i in modvals:
#     rem[i[0]] += 1
#
# # print(rem)
# cnt = 0
#
# mm1rec = []
#
# for i in range(n):
#     elem = modvals[i]
#
#     if used[elem[0]] < n//m:
#         used[elem[0]] += 1
#     else:
#         if elem[0] != m-1:
#             used[elem[0]+1] += 1
#             arr[elem[1]] += 1
#             cnt += 1
#         else:
#             used[m - 1] += 1
#             mm1rec.append(elem[1])
#
#
# if used[m-1] > n//m:
#     for i in range(m-1):
#         elem = [i, 0]
#         while used[i] < n//m:
#             # arr[elem[1]] += abs(elem[0] + 1)
#             used[i] += 1
#             used[m - 1] -= 1
#             arr[mm1rec[-1]] += abs(i + 1)
#             mm1rec.pop()
#             cnt += abs(i + 1)
#
#
# print(cnt)
#
# arrstr = [str(z) for z in arr]
#
# print(' '.join(arrstr))
#
# #print(used, mm1rec)
#
#
#
#

from collections import deque

n, m = map(int, input().split())

arr = [int(z) for z in input().split()]

mods = [0 for i in range(m)]
placement = [[] for i in range(m)]

# for i in arr:
#     mods[i % m] += 1
#
# for i in range(m):
#     mods[i] -= n//m

for i in range(n):
    mods[arr[i] % m] += 1
    placement[arr[i] % m].append(i)

cnt = 0
queue = deque()
target = n//m
for i in range(2*m):
    mod = i % m
    if mods[mod] > n//m:
        # cnt += mods[mod] - target
        for c in range(mods[mod] - target):
            queue.append([i, placement[mod][c]])
        mods[mod] = target

    elif mods[mod] < target:
        while len(queue) > 0 and mods[mod] < target:
            elem, indice = queue.popleft()
            mods[mod] += 1
            cnt += (mod - elem) % m
            arr[indice] += (mod - elem) % m

print(cnt)
print(' '.join([str(i) for i in arr]))








