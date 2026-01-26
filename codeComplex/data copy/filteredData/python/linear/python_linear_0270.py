import sys

def main(n):
    if n <= 1:
        # print("No")
        pass
        return

    # 构造一棵确定性的树，结构为“星形 + 一条链”
    # 1 作为中心节点，2..k 作为叶子，k..n 形成链，确保是树且可扩展
    d = {}
    def add_edge(u, v):
        d.setdefault(u, []).append(v)
        d.setdefault(v, []).append(u)

    # 生成边
    # 先构造一个星形：1 连接 2..min(n, n//2+1)
    limit = max(2, n // 2 + 1)
    for v in range(2, min(limit + 1, n + 1)):
        add_edge(1, v)

    # 再构造一条链：limit+1 .. n
    for u in range(limit + 1, n):
        add_edge(u, u + 1)

    # 如果边数不足 n-1（小 n 时可能），补充成线性链
    # 统计已经有的边数量
    edge_count = sum(len(adj) for adj in d.values()) // 2
    last = 1
    while edge_count < n - 1:
        nxt = last + 1
        if nxt > n:
            break
        if nxt not in d.get(last, []):
            add_edge(last, nxt)
            edge_count += 1
        last = nxt

    # 原算法逻辑开始
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
                # 没有未访问的 child，可防止死循环
                break

    if sum(visited) == n:
        # print("Yes")
        pass
        # print(len(ans))
        pass
        for c in ans:
            # print(*c)
            pass

    else:
        # print("No")
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)