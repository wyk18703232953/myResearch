import collections
import random

def main(n: int):
    # 1. 生成测试数据：构造一棵以 1 为根的树
    # a[i] 表示 i 的父节点，i 从 2 到 n
    a = [0, 0]  # a[0], a[1] 不使用，保留原结构
    for i in range(2, n + 1):
        parent = random.randint(1, i - 1)  # 生成一棵随机树
        a.append(parent)

    # 2. 构造树的邻接表
    G = collections.defaultdict(list)
    for i in range(2, len(a)):
        G[a[i]].append(i)

    # 3. 自底向上遍历（避免递归）
    nodes = []
    q = collections.deque([1])
    while q:
        node = q.popleft()
        nodes.append(node)
        for v in G[node]:
            q.append(v)

    nodes.reverse()

    # 4. DP 计算
    dp = {}
    for u in nodes:
        count = 0
        if len(G[u]) == 0:
            count += 1
        for v in G[u]:
            count += dp[v]
        dp[u] = count

    # 5. 输出结果
    res = sorted(dp.values())
    print(' '.join(map(str, res)))


if __name__ == "__main__":
    # 示例：规模为 10 的随机树
    main(10)