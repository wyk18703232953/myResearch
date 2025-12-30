from collections import defaultdict, Counter, deque
import random
import string


def solve_instance(n, m, k, P, S):
    idx = {p: i for i, p in enumerate(P, 1)}
    G = defaultdict(list)
    deg = Counter()

    # 核心逻辑与原始代码一致
    for s, i in S:
        i = int(i)
        cand = set()
        for mask in range(1 << k):
            cur = ['_'] * k
            for j in range(k):
                if (mask >> j) & 1:
                    cur[j] = s[j]
            cur_str = "".join(cur)
            if cur_str in idx:
                cand.add(idx[cur_str])

        if i not in cand:
            print("NO")
            return

        for c in cand:
            if c == i:
                continue
            G[i].append(c)
            deg[c] += 1

    ans = []
    q = deque([i for i in range(1, n + 1) if not deg[i]])
    while q:
        i = q.popleft()
        ans.append(i)
        for j in G[i]:
            deg[j] -= 1
            if not deg[j]:
                q.append(j)

    if len(ans) < n:
        print("NO")
    else:
        print("YES")
        print(*ans)


def generate_test_data(n):
    """
    根据规模 n 生成一组 (n, m, k, P, S)

    策略：
    - 固定 k = 3（可根据需要调整或随机）
    - 随机生成 n 个模式串 P，每个长度为 k，字符来自小写字母和下划线 '_'
    - 生成 m 条查询 S，使得一定有合法解：
        * 对于每个模式 P[i]，从它生成一个可以匹配它的具体串 s
          （把其中的 '_' 替换成随机字母），并令 i 为其目标编号。
        * 额外添加一些随机合法/不一定合法的查询，增加复杂度。
    """
    k = 3
    letters = string.ascii_lowercase

    # 生成 P
    P = []
    for _ in range(n):
        pattern = []
        for _ in range(k):
            # 以较大概率生成字母，较小概率生成 '_'
            if random.random() < 0.7:
                pattern.append(random.choice(letters))
            else:
                pattern.append('_')
        P.append("".join(pattern))

    # 为保证至少有一组“合理”的 S，我们先为每个 P[i] 生成一个匹配它的 s
    S = []
    for i, p in enumerate(P, start=1):
        s_chars = []
        for ch in p:
            if ch == '_':
                s_chars.append(random.choice(letters))
            else:
                s_chars.append(ch)
        s = "".join(s_chars)
        S.append([s, str(i)])

    # 再添加若干随机查询（有可能导致 NO，这没关系）
    extra = max(0, n // 2)
    for _ in range(extra):
        # 随机生成一个具体串 s
        s = "".join(random.choice(letters) for _ in range(k))
        # 随机选择一个目标索引
        i = random.randint(1, n)
        S.append([s, str(i)])

    m = len(S)
    return n, m, k, P, S


def main(n):
    # 固定随机种子以复现实验（可根据需要移除或修改）
    random.seed(0)

    n, m, k, P, S = generate_test_data(n)
    # 可以在此打印生成的数据以调试，如：
    # print(n, m, k)
    # print("\n".join(P))
    # for s, i in S:
    #     print(s, i)

    solve_instance(n, m, k, P, S)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)