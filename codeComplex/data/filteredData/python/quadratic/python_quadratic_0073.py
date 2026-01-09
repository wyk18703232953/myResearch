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

def main(n):
    """
    n: 规模参数，用作数组大小和查询数量的基准。
       这里构造：
       - 数组 a 为 1..n 的一个排列（从 1 到 n）。
       - 查询数量 q = n（每次查询区间 [1, i]）。
    """
    global ST
    # 重置线段树
    ST = [0] * (4 * maxn)

    # 生成测试数据：数组 a 为 [1, 2, ..., n]
    a = list(range(1, n + 1))

    # 初始 res 计算逻辑
    res = 0
    for x in a:
        if x + 1 <= n:
            res ^= get(1, 1, n, x + 1, n) % 2
        update(1, 1, n, x)

    # 生成测试查询数据：q = n，查询 [1, i]
    q = n
    queries = [(1, i) for i in range(1, n + 1)]

    # 输出查询结果
    for x, y in queries:
        if int((y - x) * (y - x + 1) / 2) & 1:
            res ^= 1
        if res:
            # print("odd")
            pass

        else:
            # print("even")
            pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)