import random

def main(n: int):
    # 1. 生成测试数据：构造一棵树（n 个点，n-1 条边）
    # 为了简单，将树生成为一条链或随机树均可，这里用随机树
    edges = []
    if n == 1:
        # 特殊情况：只有一个节点，没有边
        print("Yes")
        print(0)
        return
    for v in range(2, n + 1):
        u = random.randint(1, v - 1)  # 保证连通形成树
        edges.append((u, v))

    # 2. 原逻辑开始
    d = {}
    for u, v in edges:
        d.setdefault(u, []).append(v)
        d.setdefault(v, []).append(u)

    # 选度数最大的点作为 node
    node = 1
    for key in d:
        if len(d[key]) > len(d[node]):
            node = key

    ans = []
    visited = [0] * n
    visited[node - 1] = 1

    for c in d[node]:
        while True:
            visited[c - 1] = 1
            if len(d[c]) == 1:
                ans.append([node, c])
                break
            for child in d[c]:
                if visited[child - 1] != 1:
                    c = child
                    break
            else:
                # 所有 child 都访问过，防止死循环
                break

    if sum(visited) == n:
        print("Yes")
        print(len(ans))
        for c in ans:
            print(*c)
    else:
        print("No")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)