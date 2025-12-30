import random

def main(n: int):
    # 1. 生成测试数据：生成一个以 0 为根的随机树
    # p[i] 表示节点 i+1 的父亲（1-based），原代码中 p 长度为 n-1
    if n <= 0:
        return

    # 随机生成一个树的父节点数组（1-based）
    # 对于每个节点 i (1..n-1)，随机选择 [0..i-1] 中的一个作为父亲，再转为 1-based 存在 p 中
    p = []
    for i in range(1, n):
        parent = random.randint(0, i - 1)  # 0-based 父节点
        p.append(parent + 1)               # 转为 1-based 存储，和原程序一致

    # 2. 原逻辑开始（将输入改为用生成的数据 p）
    gr = [[] for _ in range(n)]
    for i in range(n - 1):
        gr[p[i] - 1].append(i + 1)

    q = [0]
    after = []
    i = 0
    s = [0 for _ in range(n)]
    used = set()
    used.add(0)

    # BFS 得到访问顺序 after
    while q:
        cur = q.pop()
        after.append(cur)
        for el in gr[cur]:
            if el not in used:
                used.add(el)
                q.append(el)
                i += 1

    # 按 after 的逆序进行 DP
    q = after
    for j in range(i, -1, -1):
        if len(gr[q[j]]) == 0:
            s[q[j]] = 1
        else:
            ans = 0
            for c in gr[q[j]]:
                ans += s[c]
            s[q[j]] = ans

    s.sort()
    print(' '.join(map(str, s)))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)