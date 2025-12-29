from collections import deque
import random


def main(n: int):
    # 1. 生成一棵随机树（n 个结点，结点编号 1..n）
    g = {i: set() for i in range(1, n + 1)}
    if n > 1:
        # 生成一棵随机树：每个节点 i 连向 [1, i-1] 中的随机一个
        for i in range(2, n + 1):
            p = random.randint(1, i - 1)
            g[p].add(i)
            g[i].add(p)

    # 2. 生成测试遍历序列 a（随机打乱 1..n）
    a = list(range(1, n + 1))
    random.shuffle(a)

    # 3. 原始逻辑
    ans = True
    if n > 1 and a[0] == 1:
        q = deque()
        m = [0] * (n + 1)
        q.append(1)
        m[1] = 1
        right = 1
        while q and ans:
            first = q.popleft()
            cnt = 0
            for v in g[first]:
                if m[v] == 0:
                    cnt += 1
            for i in range(right, right + cnt):
                if i >= n:  # 防止越界（随机 a 时可能不匹配）
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

    print("Yes" if ans else "No")


if __name__ == "__main__":
    # 示例：规模设为 10
    main(10)