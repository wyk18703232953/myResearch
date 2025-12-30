import math, sys, bisect, heapq, os
from collections import defaultdict, Counter, deque
from itertools import groupby, accumulate
from functools import lru_cache

int1 = lambda x: int(x) - 1

def aj_from_list(lst, idx):
    return list(map(int, lst[idx].split()))

def list3d(a, b, c, d):
    return [[[d] * c for _ in range(b)] for _ in range(a)]

def Y(c):
    print(["NO", "YES"][c])

def y(c):
    print(["no", "yes"][c])

def Yy(c):
    print(["No", "Yes"][c])


def main(n):
    # 生成测试数据：
    # 规模参数 n 为模式串数量
    # 设 k 为模式长度，m 为查询数量
    # 简单起见：
    #   k = max(1, min(10, n))   # 限制长度不过大
    #   m = n                    # 查询数量与模式数相同
    # 生成 n 个模式串，使用 'a','b' 和 '_'，保证唯一
    # 每个查询：(s, mt)
    #   s 从已有模式中取，mt 为其下标，保证一定有解且拓扑为 1..n

    k = max(1, min(10, n))
    m = n

    # 生成 n 个唯一模式串（只用 'a' 和 '_'，不含 'b'，便于控制）
    patterns = []
    seen = set()
    for i in range(n):
        # 用二进制计数生成模式，部分位用 '_' 代替
        b = bin(i)[2:].zfill(k)
        s = []
        for ch in b:
            if ch == '1':
                s.append('a')
            else:
                s.append('_')
        s = ''.join(s)
        # 保证唯一
        if s in seen:
            s = 'a' * k
            while s in seen:
                s = s[:-1] + '_' * (k - len(s) + 1)
        seen.add(s)
        patterns.append(s)

    # 构造查询：
    # 为了让拓扑排序结果为 1..n：
    #   对于第 i 个模式，构造一个查询 (s_i, mt=i)
    #   并保证不会产生额外边：即除 i 外，不会匹配到其他模式
    # 使用模式自身作为 s，并保证列表中不会出现其他可由 s 掩码匹配的模式
    # 在上述构造里 patterns[i] 的 '_' 分布不同且只用 'a'，基本不会互相匹配，
    # 为确保绝对安全，可以都改为不含 '_' 的查询串（将 '_' 替换成 'a'）
    queries = []
    for i in range(n):
        s = patterns[i].replace('_', 'a')
        mt = i + 1
        queries.append((s, mt))

    # 开始执行原逻辑，只是数据来自上述构造

    G = defaultdict(list)

    def addEdge(a, b):
        G[a].append(b)

    def Kahn(N):
        in_degree = [0] * (N + 1)
        for u in G.keys():
            for v in G[u]:
                in_degree[v] += 1
        queue = deque()
        for i in range(1, N + 1):
            if in_degree[i] == 0:
                queue.append(i)
        cnt = 0
        top_order = []
        while queue:
            u = queue.popleft()
            top_order.append(u)
            for v in G.get(u, []):
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
            cnt += 1
        if cnt != N:
            Y(0)
        else:
            Y(1)
            print(*top_order)

    # 构造 mark
    mark = {}
    for i in range(n):
        s = patterns[i]
        mark[s] = i + 1

    # 预计算 B（所有掩码）
    B = []
    for i in range(2 ** k):
        f = bin(i)[2:]
        f = '0' * (k - len(f)) + f
        B.append(f)

    # 处理查询
    for s, mt in queries:
        st = set()
        for mask in B:
            ss = [''] * k
            for l in range(k):
                if mask[l] == '1':
                    ss[l] = s[l]
                else:
                    ss[l] = '_'
            ss = "".join(ss)
            if ss in mark:
                st.add(mark[ss])
        if mt not in st:
            Y(0)
            return
        st.discard(mt)
        for j in st:
            addEdge(mt, j)

    Kahn(n)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)