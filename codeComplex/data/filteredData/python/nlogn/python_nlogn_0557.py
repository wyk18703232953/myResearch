from collections import deque
import random

def bfs(n, l, b):
    global visited, dp, s, ans
    while len(b) > 0 and len(s) > 0:
        aux = 0
        for i in l[s[0]]:
            if not visited[i]:
                visited[i] = True
                dp[i] = 1
                aux += 1
        for _ in range(aux):
            if not b:
                ans = "No"
                return
            x = b.popleft()
            if dp[x] == 1:
                s.append(x)
                dp[x] = -1
            else:
                ans = "No"
                return
        s.popleft()


def main(n):
    global visited, dp, s, ans

    # 1. 生成一棵随机树的边
    # 保证是连通的：每个节点 i (2..n) 随机连到 [1..i-1]
    l = [[] for _ in range(n + 2)]
    for i in range(2, n + 1):
        parent = random.randint(1, i - 1)
        l[parent].append(i)
        l[i].append(parent)

    # 2. 生成一个随机的“遍历序列” b
    # 原代码期望 b 是 1..n 的某种排列，以 1 开头
    nodes = list(range(1, n + 1))
    random.shuffle(nodes)
    if nodes[0] != 1:
        idx1 = nodes.index(1)
        nodes[0], nodes[idx1] = nodes[idx1], nodes[0]
    b = deque(nodes)
    b.popleft()  # 模拟原代码先读入整个数组，再 popleft 掉第一个元素

    # 3. 初始化与调用 bfs
    visited = [False for _ in range(n + 2)]
    dp = [-1 for _ in range(n + 2)]
    s = deque([1])
    ans = "Yes"
    visited[1] = True

    bfs(1, l, b)
    print(ans)


# 示例调用
if __name__ == "__main__":
    main(10)