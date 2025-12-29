from collections import defaultdict, deque
import random

def main(n):
    # 1. 生成测试数据（有向图，m 条边）
    # 这里给出一种简单的随机生成方式，可按需要调整：
    # - 不生成自环
    # - 边权 c 在 [0, 10^9] 内
    # - m 规模取 n 的若干倍，这里取 m = n * 2（可调整）
    m = max(1, n * 2)
    edges = []
    idx = defaultdict(lambda: deque([]))

    for i in range(m):
        u = random.randrange(n)
        v = random.randrange(n)
        while v == u:
            v = random.randrange(n)
        c = random.randint(0, 10**9)
        edges.append((u, v, c))
        idx[10**6 * u + v].append(i + 1)

    def judge(x):
        ins = [0] * n
        outs = defaultdict(list)

        for u, v, c in edges:
            if c > x:
                ins[v] += 1
                outs[u].append(v)

        q = deque([v for v in range(n) if ins[v] == 0])
        cnt = 0

        while q:
            v = q.popleft()
            cnt += 1
            for nv in outs[v]:
                ins[nv] -= 1
                if ins[nv] == 0:
                    q.append(nv)

        return cnt == n

    def binary_search():
        l, r = 0, 10**9 + 10
        while l <= r:
            m_mid = (l + r) // 2
            if judge(m_mid):
                r = m_mid - 1
            else:
                l = m_mid + 1
        return l

    k = binary_search()
    ins = [0] * n
    outs = defaultdict(list)
    removed = []

    for u, v, c in edges:
        if c > k:
            ins[v] += 1
            outs[u].append(v)
        else:
            removed.append((u, v))

    q = deque([v for v in range(n) if ins[v] == 0])
    order = [-1] * n
    cnt = 0

    while q:
        v = q.popleft()
        order[v] = cnt
        cnt += 1
        for nv in outs[v]:
            ins[nv] -= 1
            if ins[nv] == 0:
                q.append(nv)

    change = []
    for u, v in removed:
        if order[v] < order[u]:
            change.append(idx[10**6 * u + v].popleft())

    print(k, len(change))
    if change:
        print(*change)


if __name__ == "__main__":
    # 示例：运行规模 n = 5，可自行修改
    main(5)