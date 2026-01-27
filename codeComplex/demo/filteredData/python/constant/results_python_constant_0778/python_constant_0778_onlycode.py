import sys
input = sys.stdin.readline

ok = set()
for i in range(114514):
    x = i * i
    ok.add(2 * x)
    ok.add(4 * x)

t = int(input())
for _ in range(t):
    n = int(input())
    ans = "YES" if n in ok else "NO"
    print(ans)