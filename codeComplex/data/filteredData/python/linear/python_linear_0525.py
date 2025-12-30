from collections import deque
import random


def main(n: int):
    # 1. 生成一棵 n 个节点的随机树（节点编号 1..n）
    # 使用随机生成的父节点方式构造树
    g = dict()
    for i in range(1, n + 1):
        g[i] = set()

    # 保证连通且无环：对每个 2..n 随机连到 [1..i-1]
    for i in range(2, n + 1):
        p = random.randint(1, i - 1)
        g[p].add(i)
        g[i].add(p)

    # 2. 生成一个大小为 n 的访问序列 a
    # 为了测试算法逻辑，这里生成一个随机排列作为 BFS 序列候选
    # 你也可以改成专门构造正确/错误的 BFS 序列
    a = list(range(1, n + 1))
    random.shuffle(a)

    # 3. 原逻辑迁移
    ans = True
    if n > 1 and a[0] == 1:
        q = deque()
        m = [0] * (n + 1)
        q.append(1)
        m[1] = 1
        right = 1
        while len(q) > 0 and ans:
            first = q.popleft()
            cnt = 0
            for v in g[first]:
                if m[v] == 0:
                    cnt += 1
            for i in range(right, right + cnt):
                if i >= n:
                    ans = False
                    break
                if m[a[i]] == 0 and a[i] in g[first]:
                    m[a[i]] = 1
                    q.append(a[i])
                else:
                    ans = False
                    break
            right += cnt
    else:
        ans = (a[0] == 1)

    if ans:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)