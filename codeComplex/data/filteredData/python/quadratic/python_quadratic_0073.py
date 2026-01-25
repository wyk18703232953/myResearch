import sys

maxn = int(1e5 + 10)
ST = [0] * (4 * maxn)

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

def generate_input(n):
    if n <= 0:
        return 0, [], 0, []
    size = n
    arr = [i % size + 1 for i in range(size)]
    q = n
    queries = []
    for i in range(q):
        x = i % size + 1
        y = size - (i % size)
        if x > y:
            x, y = y, x
        queries.append((x, y))
    return size, arr, q, queries

def main(n):
    global ST
    ST = [0] * (4 * maxn)
    size, arr, q, queries = generate_input(n)
    res = 0
    for x in arr:
        res ^= get(1, 1, size, x + 1, size) % 2
        update(1, 1, size, x)
    out_lines = []
    for x, y in queries:
        if ((y - x) * (y - x + 1) // 2) & 1:
            res ^= 1
        if res:
            out_lines.append("odd")
        else:
            out_lines.append("even")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main(10)