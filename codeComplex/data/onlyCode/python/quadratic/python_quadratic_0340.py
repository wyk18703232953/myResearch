import sys, string

def swap(i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

n = int(sys.stdin.readline())
a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())
res_a = dict().fromkeys(list(string.ascii_lowercase), 0)
res_b = dict().fromkeys(list(string.ascii_lowercase), 0)

for i in a:
    res_a[i] += 1
for i in b:
    res_b[i] += 1

can = True
for i in res_a:
    if res_a[i] != res_b[i]:
        can = False
        break
if not can:
    print(-1)
else:
    ans = []
    for i in range(n):
        if a[i] == b[i]:
            continue
        else:
            idx = -1
            for j in range(i + 1, n):
                if a[j] == b[i]:
                    idx = j
                    break
            for j in range(idx, i, -1):
                ans.append(j)
                swap(j, j - 1)
    print(len(ans))
    print(' '.join(map(str, ans)))

