from sys import stdin

rints = lambda: [int(x) for x in stdin.readline().split()]
n, A, B, C, T = rints()
a, ans = rints(), 0
for i in range(n):
    su, cur = A, A
    for j in range(a[i], T):
        cur -= B
        su = max(su, (j - a[i] + 1) * C + cur)

    ans += su
print(ans)
