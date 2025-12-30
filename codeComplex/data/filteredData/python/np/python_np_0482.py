from collections import defaultdict, deque, Counter
import random
import string


def toposort(graph):
    res = []
    found = [0] * len(graph)
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            res.append(~node)
        elif not found[node]:
            found[node] = 1
            stack.append(~node)
            stack += graph[node]

    # cycle check
    for node in res:
        if any(found[nei] for nei in graph[node]):
            return None
        found[node] = 0

    return res[::-1]


def solve(N, M, K, P, S, MT):
    graph = [[] for _ in range(N)]

    def isMatch(s, pattern):
        for a, b in zip(s, pattern):
            if b != "_" and a != b:
                return False
        return True

    ordA = ord("a") - 1

    def hashStr(s):
        hsh = 0
        for c in s:
            val = 27 if c == "_" else ord(c) - ordA
            hsh = 32 * hsh + val
        return hsh

    patternToId = {}
    for i, p in enumerate(P):
        patternToId[hashStr(p)] = i

    for s, mt in zip(S, MT):
        if not isMatch(s, P[mt]):
            return "NO"
        vals = [ord(c) - ordA for c in s]
        for mask in range(1 << K):
            hsh = 0
            for pos in range(K):
                val = 27 if (1 << pos) & mask else vals[pos]
                hsh = 32 * hsh + val
            if hsh in patternToId:
                mt2 = patternToId[hsh]
                if mt2 != mt:
                    graph[mt].append(mt2)

    ans = toposort(graph)
    if ans is None:
        return "NO"

    return "YES\n" + " ".join(str(i + 1) for i in ans)


def generate_test_data(n):
    """
    根据规模 n 生成一组 (N, M, K, P, S, MT) 测试数据。
    这里将:
      N = n
      K = min(4, n)  固定较小串长，便于生成
      M = n
    """
    N = n
    K = min(4, n if n > 0 else 1)
    M = n

    letters = string.ascii_lowercase[:3]  # 使用少量字母，提升匹配几率

    def random_pattern():
        return "".join(random.choice(letters + "_") for _ in range(K))

    def random_string():
        return "".join(random.choice(letters) for _ in range(K))

    # 生成 N 个模式 P
    P = [random_pattern() for _ in range(N)]

    # 生成 M 个 (字符串, 模式索引)，尽量保证有一定概率合法
    S = []
    MT = []
    for _ in range(M):
        mt = random.randrange(N)
        base = P[mt]
        s_list = []
        for c in base:
            if c == "_":
                s_list.append(random.choice(letters))
            else:
                # 有较大概率保持匹配，少量概率破坏匹配
                if random.random() < 0.8:
                    s_list.append(c)
                else:
                    s_list.append(random.choice([x for x in letters if x != c]))
        s = "".join(s_list)
        S.append(s)
        MT.append(mt)

    return N, M, K, P, S, MT


def main(n):
    N, M, K, P, S, MT = generate_test_data(n)
    result = solve(N, M, K, P, S, MT)
    print(result)


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)