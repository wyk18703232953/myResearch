R = lambda: map(int, input().split())
n, s = R()
l, r = s, 10**18 + 7

def digit(x):
    res = 0
    while x:
        res += x % 10
        x //= 10
    return res

while l < r:
    m = (l + r) // 2
    if m - digit(m) < s:
        l = m + 1
    else:
        r = m
print(max(0, n - l + 1))