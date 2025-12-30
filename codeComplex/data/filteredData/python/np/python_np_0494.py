import random
from collections import defaultdict, deque

def main(n):
    # 生成测试数据：
    # n: 模板字符串数量
    # m: 查询数量，取 n 的 2 倍
    # k: 字符串长度，固定为 3（也可改为其他小整数）
    k = 3
    m = max(1, 2 * n)

    # 生成 n 个长度为 k 的模板串（字符从 'a'..'c'）
    def random_pattern(k):
        return ''.join(random.choice('abc') for _ in range(k))

    templates = [random_pattern(k) for _ in range(n)]

    # 构造 m 个查询 (S, t)
    # 为了有一定概率生成 YES 的情况，部分查询 S 为模板串，
    # 部分为随机串，t 在 [1, n] 中随机选。
    queries = []
    for _ in range(m):
        if random.random() < 0.7:  # 70% 概率用已有模板串
            S = random.choice(templates)
        else:
            S = random_pattern(k)
        t = random.randint(1, n)
        queries.append((S, t))

    # ===== 以下为原逻辑的无 input() 改写 =====

    def edges(s):
        Ans = set()
        for i in range(2 ** k):
            ans = ''
            for j in range(k):
                if i >> j & 1:
                    ans = ''.join([ans, s[j]])
                else:
                    ans = ''.join([ans, '_'])
            Ans.add(ans)
        return Ans

    D = defaultdict(lambda: -1)
    for i in range(n):
        D[templates[i]] = i

    flag = 1
    In = [set() for _ in range(n)]
    Out = [set() for _ in range(n)]

    for S, t in queries:
        for e in edges(S):
            if D[e] + 1:
                Out[t - 1].add(D[e])
                In[D[e]].add(t - 1)
        if (t - 1) not in Out[t - 1]:
            flag = 0
            break
        else:
            Out[t - 1].remove(t - 1)
            In[t - 1].remove(t - 1)

    def topological_sort(In, Out):
        dq = deque()
        L = []
        for i, I in enumerate(In):
            if not I:
                dq.append(i)
        while dq:
            v = dq.popleft()
            L.append(v)
            for w in list(Out[v]):
                if v in In[w]:
                    In[w].remove(v)
                if not In[w]:
                    dq.append(w)
        if len(L) < len(In):
            return False
        return L

    T = topological_sort(In, Out)
    if flag == 0 or not T:
        print('NO')
    else:
        print('YES')
        print(*[t + 1 for t in T], sep=' ')

if __name__ == "__main__":
    # 示例：以 n = 5 运行
    main(5)