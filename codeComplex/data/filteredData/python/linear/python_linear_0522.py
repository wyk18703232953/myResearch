import random

def main(n):
    # 1. 生成一棵有 n 个节点的随机树（节点编号 1..n）
    # 使用随机生成的父节点构造一棵树
    dict1 = {}
    for i in range(1, n + 1):
        dict1[i] = []
    # 生成树的边：对于每个节点 i(2..n)，随机选择 [1..i-1] 中的一个父节点
    for child in range(2, n + 1):
        parent = random.randint(1, child - 1)
        dict1[parent].append(child)
        dict1[child].append(parent)

    # 2. 根据 dict1 生成一个 BFS 序列，保证是合法序列
    # BFS 从 1 开始
    from collections import deque
    visited = [False] * (n + 1)
    q = deque([1])
    visited[1] = True
    bfs_order = []
    while q:
        node = q.popleft()
        bfs_order.append(node)
        # 为了多样性打乱邻居顺序
        neighbors = list(dict1[node])
        random.shuffle(neighbors)
        for nei in neighbors:
            if not visited[nei]:
                visited[nei] = True
                q.append(nei)

    # 将 bfs_order 作为 arr（原程序中的输入序列）
    arr = bfs_order

    # 3. 按原程序逻辑运行判断
    if arr[0] != 1:
        print("No")
        return

    j = 0
    i = 1
    while i < n and j < n:
        if arr[i] in dict1[arr[j]]:
            i += 1
        else:
            j += 1
    if i != n and j == n:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)