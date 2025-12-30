from collections import deque
import random


def main(n: int):
    # 生成测试数据：
    # 合理地选择 d, k，使得大部分情况下可以构造出树，便于测试。
    # 例如：
    #   d: 直径，介于 1 和 min(n-1, 15) 之间
    #   k: 最大度数，介于 2 和 min(n, 10) 之间
    if n < 2:
        # 原题至少需要 n>=2 才有意义
        print("NO")
        return

    d = random.randint(1, min(n - 1, 15))
    k = random.randint(2, min(n, 10))

    # 下面是原逻辑的改写（移除 input，封装到 main 中）

    if d >= n:
        print("NO")
        return

    graph = [[] for _ in range(n + 1)]

    for i in range(1, d + 2):
        graph[i].append(min(i - 1, d + 1 - i))

    for i in range(1, d + 1):
        graph[i].append(i + 1)
        graph[i + 1].append(i)

    deg = [0] * (n + 1)
    deg[1] = 1
    deg[d + 1] = 1
    for i in range(2, d + 1):
        deg[i] = 2

    for v in deg:
        if v > k:
            print("NO")
            return

    p = d + 2
    for i in range(1, d + 2):
        q = deque()
        q.append(i)
        while q:
            x = q.popleft()
            # graph[x][0] 是该节点与“层数”（或与根的距离）有关的一个值
            while graph[x][0] > 0 and deg[x] < k and p <= n:
                graph[x].append(p)
                deg[x] += 1
                graph[p].append(graph[x][0] - 1)
                graph[p].append(x)
                deg[p] += 1
                q.append(p)
                p += 1

    if p <= n:
        print("NO")
        return

    print("YES")
    vis = [-1] * (n + 1)

    for i in range(1, d + 2):
        if vis[i] == -1:
            q = deque()
            q.append(i)
            while q:
                x = q.popleft()
                vis[x] = 1
                for j in range(1, len(graph[x])):
                    to = graph[x][j]
                    if vis[to] == -1:
                        print(x, to)
                        q.append(to)


# 需要时可在此调试：
# if __name__ == "__main__":
#     main(10)