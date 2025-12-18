import io, sys
input = lambda f=io.StringIO(sys.stdin.buffer.read().decode()).readline: f().rstrip()

ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())

n, k = mi()
a = li()
d = [a[i + 1] - a[i] for i in range(n - 1)]
ans = sum(sorted(d)[:n - 1 - (k - 1)])
print(ans)