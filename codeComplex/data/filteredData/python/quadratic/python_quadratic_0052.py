def inv_cnt(b):
    c = 0
    visited = set()
    for i in range(len(b)):
        if i + 1 in visited:
            continue
        visited.add(i + 1)
        path = [i + 1]
        while b[path[-1] - 1] != path[0]:
            visited.add(b[path[-1] - 1])
            path.append(b[path[-1] - 1])
        c += len(path) - 1
    return c % 2


def main(n):
    # 1. 生成测试数据
    # 生成一个 1..n 的排列作为数组 a
    a = list(range(1, n + 1))

    # 基于 a 的初始逆序奇偶值
    x = inv_cnt(a)

    # 生成若干区间查询，这里简单设为 n 个查询
    m = n
    queries = []
    for i in range(m):
        # 生成一个区间 [l, r]，保证 1 <= l <= r <= n
        # 示例：循环生成一些覆盖不同长度的区间
        l = i % n + 1
        r = n
        queries.append((l, r))

    # 2. 按照原题逻辑处理查询并打印结果
    for l, r in queries:
        x = (x + (r - l + 1) // 2) % 2
        if x:
            # print("odd")
            pass

        else:
            # print("even")
            pass
if __name__ == "__main__":
    # 示例：调用 main(5)，可按需要修改或在外部调用 main(n)
    main(5)