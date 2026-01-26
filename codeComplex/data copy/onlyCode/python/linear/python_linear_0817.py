import io, sys
input = lambda f=io.StringIO(sys.stdin.buffer.read().decode()).readline: f().rstrip()
 
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())

n, k = mi()
ans = None
for x in range(1, n + 1):
    if x * (x + 3) == 2 * (k + n):
        ans = n - x
        break
print(ans)