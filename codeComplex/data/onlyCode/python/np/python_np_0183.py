n, l, r, x = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
for j in range(1, 2**n):
    a = [arr[i] for i in range(n) if (((j >> i) & 1) == 1)]
    res += (max(a) - min(a) >= x and sum(a) >= l and sum(a) <= r)
print(res)
