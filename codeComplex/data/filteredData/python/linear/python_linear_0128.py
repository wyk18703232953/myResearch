import random

def if_spruce(n, l, s):
    d = [0] * (n + 1)
    for i in range(1, n + 1):
        if i not in s:          # i 是叶子
            d[l[i]] += 1        # 给它的父亲叶子计数 +1
    for i in range(1, n + 1):
        if i in s and d[i] < 3: # i 是内部节点但叶子孩子少于 3 个
            return "No"
    return "Yes"

def main(n):
    # 生成一棵以 1 为根的随机树（父节点数组 l，1..n）
    # l[i] 表示节点 i 的父亲；其中 l[1] = 0 作为占位（根无父）
    l = [0, 0]  # 从索引 2 开始存真实父亲，索引 1 的父亲设为 0
    for i in range(2, n + 1):
        parent = random.randint(1, i - 1)
        l.append(parent)

    # s 是内部节点集合（有孩子的节点）：根据树结构生成
    s = set()
    for child in range(2, n + 1):
        s.add(l[child])

    ans = if_spruce(n, l, s)
    print(ans)

if __name__ == "__main__":
    # 示例：可在此修改规模 n 进行测试
    main(10)