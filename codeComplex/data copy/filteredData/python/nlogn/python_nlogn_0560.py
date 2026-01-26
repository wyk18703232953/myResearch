import sys
from collections import deque

def main(n):
    # n: number of nodes in the tree
    if n < 1:
        return

    # 构造一棵确定性的树：1-2, 2-3, ..., (n-1)-n（链状树）
    visited = [False for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]
    l = [[] for _ in range(n + 1)]
    for i in range(1, n):
        a = i
        b_edge = i + 1
        l[a].append(b_edge)
        l[b_edge].append(a)

    # 构造一个确定性的 BFS 序列 b
    # 使用队列按节点编号从小到大的顺序 BFS
    q = deque([1])
    visited_bfs = [False for _ in range(n + 1)]
    visited_bfs[1] = True
    b = []
    while q:
        u = q.popleft()
        b.append(u)
        for v in sorted(l[u]):  # 排序保证确定性
            if not visited_bfs[v]:
                visited_bfs[v] = True
                q.append(v)

    # 核心算法逻辑（原程序的主体），仅将输入替换为上面构造的数据
    visited = [False for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]
    s = [1]
    visited[1] = True
    c = 1
    c1 = 0
    while len(s) != n:
        aux = 0
        for i in l[s[c1]]:
            if not visited[i]:
                visited[i] = True
                dp[i] = 1
                aux += 1
        for i in range(c, c + aux):
            if dp[b[i]] == 1:
                s.append(b[i])
                dp[b[i]] = 0

            else:
                # print("No")
                pass
                return
        c += aux
        c1 += 1
    # print("Yes")
    pass
if __name__ == "__main__":
    # 示例调用：可按需要修改 n 规模进行实验
    main(10)