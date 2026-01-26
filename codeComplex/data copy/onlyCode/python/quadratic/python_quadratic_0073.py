import sys
input = sys.stdin.readline
maxn = int(1e5 + 10)
ST = [0] * (4 * maxn)
def update(id, l, r, val):
    if l == r == val:
        ST[id] = 1
        return
    if l > val or r < val:
        return
    mid = int((l + r) / 2)
    update(id * 2, l, mid, val)
    update(id * 2 + 1, mid + 1, r, val)
    ST[id] = ST[id * 2] + ST[id * 2 + 1]
    return
def get(id, l, r, x, y):
    if l > y or r < x:
        return 0
    if x <= l and r <= y:
        return ST[id]
    mid = int((l + r) / 2)
    return get(id * 2, l, mid, x, y) + get(id * 2 + 1, mid + 1, r, x, y)
n, res = int(input()), 0
for x in list(map(int, input().split())):
    res ^= get(1, 1, n, x + 1, n) % 2
    update(1, 1, n, x)
for i in range (int(input())):
    x, y = list(map(int, input().split()))
    if int((y - x) * (y - x + 1) / 2) & 1:
        res ^= 1
    if res:
        print("odd")
    else:
        print("even")