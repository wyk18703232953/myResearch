import io, sys
input = lambda f=io.StringIO(sys.stdin.buffer.read().decode()).readline: f().rstrip()

ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())

n, m, k = mi()
a = [None] + li()
p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = p[i - 1] + a[i]
s = [10 ** 16 for _ in range(m)]
s[0] = k
ans = 0
for i in range(1, n + 1):
    ans = max(ans, p[i] - min(s))
    s[i % m] = min(s[i % m], p[i])
    s[i % m] += k
print(ans)
