import sys

maxn = 1510
ST = [0 for _ in range(4 * maxn)]

def update(id, l, r, val):
    if l == r == val:
        ST[id] = 1
        return
    if l > val or r < val:
        return
    mid = (l + r) // 2
    update(id * 2, l, mid, val)
    update(id * 2 + 1, mid + 1, r, val)
    ST[id] = ST[id * 2] + ST[id * 2 + 1]

def get(id, l, r, x, y):
    if l > y or r < x:
        return 0
    if x <= l and r <= y:
        return ST[id]
    mid = (l + r) // 2
    return get(id * 2, l, mid, x, y) + get(id * 2 + 1, mid + 1, r, x, y)

def main(n):
    global ST
    if n <= 0:
        return
    ST = [0 for _ in range(4 * (n + 5))]
    arr = [i % n + 1 for i in range(n)]
    res = 0
    for x in arr:
        res ^= get(1, 1, n, x + 1, n) % 2
        update(1, 1, n, x)
    q = n
    outputs = []
    for i in range(q):
        x = i + 1
        y = n
        if ((y - x) * (y - x + 1) // 2) & 1:
            res ^= 1
        if res:
            outputs.append("odd")
        else:
            outputs.append("even")
    for line in outputs:
        print(line)

if __name__ == "__main__":
    main(10)