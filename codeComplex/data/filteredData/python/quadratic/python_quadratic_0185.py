def main(n):
    # n 表示初始数组 a 的长度
    if n <= 0:
        return

    # 确定性生成长度为 n 的数组 a
    # 这里使用简单的算术构造：a[i] = (i * 3 + 1) % 1000
    a = [(i * 3 + 1) % 1000 for i in range(n)]

    array = []
    array.append(a)

    # 构造基于相邻异或的三角形结构
    for _ in range(n - 1):
        aux = []
        for j in range(1, len(array[-1])):
            x = array[-1][j - 1] ^ array[-1][j]
            aux.append(x)
        array.append(aux)

    # 对每一层应用 max 传递规则
    for j in range(1, len(array)):
        for k in range(len(array[j])):
            m = max(array[j][k], array[j - 1][k], array[j - 1][k + 1])
            array[j][k] = m

    # 生成确定性的查询数量 q
    # 为了保证可规模化，这里令 q 与 n 同阶：q = n
    q = n

    # 生成 q 个确定性区间查询 (l, r)，满足 1 <= l <= r <= n
    queries = []
    for i in range(1, q + 1):
        # 使用简单的算术构造生成 l, r
        l = (i % n) + 1
        r = n - (i % n)
        if l > r:
            l, r = r, l
        if l < 1:
            l = 1
        if r > n:
            r = n
        if l > r:
            l = r = (i % n) + 1
        queries.append((l, r))

    # 按原逻辑输出查询结果
    for l, r in queries:
        # print(str(array[r - l][l - 1]))
        pass
if __name__ == "__main__":
    # 示例规模调用，可按需修改 n 进行实验
    main(10)