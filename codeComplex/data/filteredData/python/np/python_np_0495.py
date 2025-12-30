from collections import deque, defaultdict
import random
import string

def topological_sort(In, Out):
    dq, L = deque(), []
    for i, I in enumerate(In):
        if not I:
            dq.append(i)
    while dq:
        v = dq.popleft()
        L.append(v)
        for w in Out[v]:
            In[w].remove(v)
            if not In[w]:
                dq.append(w)
    if len(L) < len(In):
        return False
    return L

def main(n):
    # 生成规模参数
    # n: 模板数量
    # k: 模板长度
    # m: 约束数量
    k = max(1, min(5, n if isinstance(n, int) else 5))
    m = max(1, n)  # 生成 m 条约束

    # 生成 n 个长度为 k 的模板串（由小写字母与 '_' 构成）
    # 为了提高可匹配性，保证字符集较小
    chars = string.ascii_lowercase[:3] + '_'
    templates = set()
    while len(templates) < n:
        s = ''.join(random.choice(chars) for _ in range(k))
        templates.add(s)
    templates = list(templates)

    # 构造字典 D：模板 -> 下标
    D = defaultdict(lambda: -1)
    for i, s in enumerate(templates):
        D[s] = i

    # 辅助函数：生成所有模式（边）
    def edges(s):
        Ans = set()
        for mask in range(1 << k):
            ans = []
            for j in range(k):
                if (mask >> j) & 1:
                    ans.append(s[j])
                else:
                    ans.append('_')
            Ans.add(''.join(ans))
        return Ans

    # 生成 m 条约束 (S, t)
    # t 为 1..n 的随机下标（1-based）
    constraints = []
    for _ in range(m):
        t = random.randint(1, n)
        # 为了提高匹配概率，从已有模板中选一个并随机替换部分字符为 '_'
        base = templates[random.randint(0, n - 1)]
        s_list = list(base)
        for j in range(k):
            if random.random() < 0.3:
                s_list[j] = random.choice(chars)
        S = ''.join(s_list)
        constraints.append((S, t))

    flag = 1
    In = [set() for _ in range(n)]
    Out = [set() for _ in range(n)]

    for S, t in constraints:
        t_idx = t - 1
        for e in edges(S):
            if D[e] + 1:  # 存在该模式
                Out[t_idx].add(D[e])
                In[D[e]].add(t_idx)
        # 原逻辑的自环检查
        if t_idx not in Out[t_idx]:
            flag = 0
            break
        else:
            Out[t_idx].remove(t_idx)
            In[t_idx].remove(t_idx)

    T = topological_sort(In, Out)
    if flag == 0 or not T:
        print('NO')
    else:
        print('YES')
        print(*[t + 1 for t in T], sep=' ')

if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)