def main(n):
    import random

    C = 10**9 + 7

    # 生成测试数据
    # 随机生成长度为 n 的 0/1 串
    lst = [random.randint(0, 1) for _ in range(n)]

    # 设定查询数量 q，并随机生成 q 个区间查询
    # 为了规模合适，这里设 q = n（可按需修改）
    q = n
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 前缀统计 0 和 1 的个数
    new_lst = [(0, 0)]
    for i in lst:
        if i == 0:
            new_lst.append((new_lst[-1][0] + 1, new_lst[-1][1]))
        else:
            new_lst.append((new_lst[-1][0], new_lst[-1][1] + 1))

    # 预计算 2 的幂
    ls = [1]
    for _ in range(n):
        ls.append(ls[-1] * 2 % C)

    # 处理查询，输出结果
    for l, r in queries:
        zeros = new_lst[r][0] - new_lst[l - 1][0]
        ones = new_lst[r][1] - new_lst[l - 1][1]
        total = zeros + ones
        print((ls[total] - ls[zeros]) % C)


if __name__ == "__main__":
    # 示例调用：可以在此修改 n 的大小进行测试
    main(10)