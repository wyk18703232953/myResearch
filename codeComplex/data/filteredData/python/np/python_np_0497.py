# Converted version: no input(), main(n) with generated test data

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


def generate_test_data(n):
    """
    根据规模 n 生成一组 (n, m, k, patterns, queries) 测试数据：
    - k: 固定一个较小值，保证 2^k 可控
    - patterns: n 个长度为 k 的字符串，仅包含小写字母和 '_'
    - queries: m 条 (S, t) 约束，S 为长度为 k 的模式，t 为 1..n 的整数
    """
    k = 3  # 可按需调整，保持 2^k 不太大
    # 生成 n 个模式串，保证互不相同
    possible_chars = string.ascii_lowercase
    patterns_set = set()
    patterns = []
    while len(patterns) < n:
        s = ''.join(random.choice(possible_chars) for _ in range(k))
        if s not in patterns_set:
            patterns_set.add(s)
            patterns.append(s)

    # 生成 m 条约束，m 大致与 n 同级
    m = max(1, n * 2)
    queries = []
    for _ in range(m):
        # 随机生成一个带 '_' 的模式
        s_list = list(random.choice(patterns))
        # 随机将若干位置变成 '_'
        for i in range(k):
            if random.random() < 0.3:
                s_list[i] = '_'
        S = ''.join(s_list)

        # 随机 t
        t = random.randint(1, n)
        queries.append((S, t))

    return n, m, k, patterns, queries


def main(n):
    # 生成测试数据
    n, m, k, patterns, queries = generate_test_data(n)

    def edges(s):
        Ans = set()
        for i in range(2 ** k):
            ans = [s[j] if i >> j & 1 else '_' for j in range(k)]
            Ans.add(''.join(ans))
        return Ans

    D = defaultdict(lambda: -1)
    for i in range(n):
        D[patterns[i]] = i

    flag = 1
    In, Out = [set() for _ in range(n)], [set() for _ in range(n)]
    for S, t in queries:
        for e in edges(S):
            if D[e] + 1:
                Out[t - 1].add(D[e])
                In[D[e]].add(t - 1)
        if t - 1 not in Out[t - 1]:
            flag = 0
            break
        else:
            Out[t - 1].remove(t - 1)
            In[t - 1].remove(t - 1)

    T = topological_sort(In, Out)
    if flag and T:
        print('YES')
        print(*[t + 1 for t in T], sep=' ')
    else:
        print('NO')


if __name__ == "__main__":
    # 示例调用：可调整 n
    main(5)