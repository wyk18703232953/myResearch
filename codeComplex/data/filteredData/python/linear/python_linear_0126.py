def if_spruce(n, l, m):
    d = [0] * (n + 1)
    for i in range(1, n + 1):
        if m[i] == 0:
            d[l[i]] += 1
    for i in range(1, n + 1):
        if m[i] > 0 and d[i] < 3:
            return "No"
    return "Yes"


def main(n):
    # 生成一棵有 n 个节点的树，父节点编号总是小于子节点编号
    # 这保证数据合法且和原来输入格式一致
    l = [0, 0]          # 下标从 1 开始，l[i] 是结点 i 的父节点；根节点 1 的父节点设为 0
    m = [0] * (n + 1)   # m[i] 是结点 i 的子节点数量

    for child in range(2, n + 1):
        # 简单生成：每个节点的父节点在 [1, child-1] 中任选一个
        # 这里固定用 child // 2，保证是树结构
        parent = child // 2
        l.append(parent)
        m[parent] += 1

    result = if_spruce(n, l, m)
    print(result)


# 示例调用
if __name__ == "__main__":
    main(10)