def main(n):
    from operator import xor

    if n <= 0:
        return

    # 数据规模设计：
    # 初始数组长度设为 n
    # 查询数量设为 n
    # 数组元素为确定性构造：a0[i] = (i * 3 + 1) % 1000
    length = n
    m = n

    # 构造初始数组 a[0]
    a0 = [(i * 3 + 1) % 1000 for i in range(length)]
    a = [a0]

    # 生成查询区间 qur，保证 1 <= l <= r <= length
    # 使用简单算术关系使其确定：
    # l_i = (i % length) + 1
    # r_i = ((i * 2) % length) + 1
    # 如果 r_i < l_i，交换
    qur = []
    for i in range(m):
        l = (i % length) + 1
        r = ((i * 2) % length) + 1
        if r < l:
            l, r = r, l
        qur.append((l, r))

    # 保持原算法逻辑：
    # 第一步：构造逐层异或的三角形
    for i in range(1, n):
        if len(a[-1]) <= 1:
            a.append([])

        else:
            a.append(list(map(xor, a[-1][:-1], a[-1][1:])))

    # 第二步：用 max 更新各层
    for i in range(n - 1):
        if i + 1 >= len(a):
            break
        if len(a[i]) <= 1:
            a[i + 1] = []

        else:
            a[i + 1] = list(map(max, a[i][:-1], a[i][1:], a[i + 1]))

    # 处理查询
    out = []
    for l, r in qur:
        # 限制在合法范围内，避免越界
        if l < 1:
            l = 1
        if r > length:
            r = length
        if r < l:
            l, r = r, l

        k = r - l
        if k < 0 or k >= len(a):
            out.append(0)
            continue
        row = a[k]
        if l - 1 < 0 or l - 1 >= len(row):
            out.append(0)

        else:
            out.append(row[l - 1])

    for v in out:
        # print(v)
        pass
if __name__ == "__main__":
    # 示例：使用 n = 5 运行一次
    main(5)