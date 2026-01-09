def main(n):
    maxn = n + 5
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

    # 构造确定性的输入数组（原来是长度为 n 的排列/序列）
    # 使用简单的确定性构造：a[i] = (i*2 mod n) + 1，保证落在 [1, n]
    arr = [((i * 2) % n) + 1 for i in range(n)]

    res = 0
    for x in arr:
        if x + 1 <= n:
            res ^= get(1, 1, n, x + 1, n) % 2
        update(1, 1, n, x)

    # 构造确定性的查询数量 q 与区间 [x, y]
    # 让 q 与 n 同阶：q = n
    q = n
    outputs = []
    for i in range(q):
        # 确定性区间构造：x 从 1..n 周期，长度随 i 变化
        x = (i % n) + 1
        length = (i // 2) % n
        y = x + length
        if y > n:
            y = n
        if ((y - x) * (y - x + 1) // 2) & 1:
            res ^= 1
        if res:
            outputs.append("odd")

        else:
            outputs.append("even")

    # 为了防止优化掉计算，统一打印结果摘要
    # 打印最后一个状态及总 odd/even 计数
    odd_count = sum(1 for v in outputs if v == "odd")
    even_count = q - odd_count
    # print(outputs[-1])
    pass
    # print(odd_count, even_count)
    pass
if __name__ == "__main__":
    main(1000)