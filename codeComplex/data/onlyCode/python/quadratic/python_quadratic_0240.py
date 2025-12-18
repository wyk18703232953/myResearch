n = int(input())
ls1 = [int(i) for i in input().split()]
ls2 = [int(i) for i in input().split()]

ans = float('inf')

for i in range(1, n - 1):
    l = [ls2[j] for j in range(0, i) if ls1[j] < ls1[i]]
    r = [ls2[j] for j in range(i + 1, n) if ls1[j] > ls1[i]]

    if len(l) and len(r):
        ans = min(ans, min(l) + min(r) + ls2[i])

print([-1 , ans][ans != float('inf')])