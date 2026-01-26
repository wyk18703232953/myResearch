import sys
input = sys.stdin.readline

def binary_search(c1, c2):
    m = (c1 + c2 + 1) // 2
    while abs(c1 - c2) > 1:
        m = (c1 + c2 + 1) // 2
        if ok(m):
            c2 = m
        else:
            c1 = m
    ans = check(m)
    return ans

def ok(m):
    s0 = m
    for i in list(str(m)):
        s0 -= int(i)
    return True if s0 > s else False

def check(m):
    for i in range(max(0, m - 5), m + 6):
        if ok(i):
            return max(0, n - i + 1)
    return 0

n, s = map(int, input().split())
if not s % 9:
    s -= 1
ans = binary_search(0, n + 1)
print(ans)