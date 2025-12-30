import random

def main(n):
    # 生成测试数据：构造一棵 n 个节点的树
    # 节点编号 1..n，随机生成一棵树
    edges = []
    if n >= 2:
        for i in range(2, n + 1):
            # 随机连到前面任意一个节点，保证连通无环
            v = random.randint(1, i - 1)
            c = i
            edges.append((v, c))

    # 原逻辑开始
    a = n
    s = {}
    ans = 0

    # 构建无向图
    for v, c in edges:
        if v in s:
            s[v].append(c)
        else:
            s[v] = [c]
        if c in s:
            s[c].append(v)
        else:
            s[c] = [v]

    # 确保每个点在字典中，即便度数为 0（n=1 时）
    for i in range(1, a + 1):
        if i not in s:
            s[i] = []

    c = 0
    for i in range(1, a + 1):
        if len(s[i]) > 2:
            c += 1
            ans = i

    if c > 1:
        print("No")
    elif c == 0:
        print("Yes")
        print(1)
        leaves = []
        for i in s:
            if len(s[i]) == 1 or a == 1:  # a==1 时唯一节点视作叶子
                leaves.append(i)
        # 原代码直接 print(i, end=" ")，这里统一换行输出
        # 以保持更清晰的输出（若需完全复刻可改回同一行）
        for i in leaves:
            print(i, end=" ")
        print()
    else:
        print("Yes")
        print(len(s[ans]))
        k = []
        for i in s:
            if len(s[i]) == 1:
                k.append(i)
        for i in k:
            print(min(ans, i), max(ans, i))


if __name__ == "__main__":
    # 示例调用：可修改 n 测试不同规模
    main(5)