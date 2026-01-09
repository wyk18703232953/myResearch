def main(n: int):
    # 生成测试数据：长度为 2*n 的列表 l
    # 这里简单生成 [1, 2, ..., n, 1, 2, ..., n]
    l = list(range(1, n + 1)) + list(range(1, n + 1))

    ans = 0
    m = []

    # 原逻辑：从后往前遍历，记录第一次出现的元素，保持逆序去重
    for i in range(2 * n - 1, -1, -1):
        if l[i] not in m:
            m.append(l[i])

    # 原逻辑：根据 m 中的前 n 个元素，在 l 中做索引/插入/删除操作并累加 ans
    for tt in range(0, n):
        i = m[tt]
        j = l.index(i)
        l.pop(j)
        k = l.index(i)
        l.insert(k, j)
        ans += k - j

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(5)，可按需要修改或在其他地方导入调用
    main(5)