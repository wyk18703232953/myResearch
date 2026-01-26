from itertools import groupby

n = int(input())
l = list(map(int, input().split()))
r = list(map(int, input().split()))
sums = [(a + b, ind) for (ind, (a, b)) in enumerate(zip(l, r))]
sums.sort()
answer = [None] * n
curr_candies = n
for key, group in groupby(sums, key=lambda i: i[0]):
    for elem in group:
        answer[elem[1]] = curr_candies
    curr_candies -= 1
tl = []
for i in range(n):
    cnt = 0
    for j in range(i):
        if answer[j] > answer[i]:
            cnt += 1
    tl.append(cnt)
tr = []
for i in range(n):
    cnt = 0
    for j in range(i + 1, n):
        if answer[j] > answer[i]:
            cnt += 1
    tr.append(cnt)
if tl != l or tr != r:
    print("NO")
else:
    print("YES")
    print(' '.join(map(str, answer)))
