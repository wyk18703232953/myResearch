n = int(input())
a = list(map(int, input().split()))
m = int(input())
parity = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            parity ^= 1
res = []
for _ in range(m):
    l, r = map(int, input().split())
    s = r - l + 1
    parity ^= (s * (s - 1) // 2) % 2
    res.append("odd" if parity else "even")
print("\n".join(res))