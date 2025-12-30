import random

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
    # 生成测试数据：长度为 n 的排列
    arr = list(range(1, n + 1))
    random.shuffle(arr)

    # 重置线段树
    global ST
    ST = [0 for _ in range(4 * maxn)]

    res = 0
    for x in arr:
        res ^= get(1, 1, n, x + 1, n) % 2
        update(1, 1, n, x)

    # 生成若干随机查询，数量可根据 n 调整，这里设为 q = n
    q = n
    queries = []
    for _ in range(q):
        x = random.randint(1, n)
        y = random.randint(1, n)
        if x > y:
            x, y = y, x
        queries.append((x, y))

    # 输出查询结果（与原逻辑保持一致）
    for x, y in queries:
        if ((y - x) * (y - x + 1) // 2) & 1:
            res ^= 1
        if res:
            print("odd")
        else:
            print("even")

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)