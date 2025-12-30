mod = 1000000007
eps = 10 ** -9


def main(n):
    """
    规模参数 n：
    - 使用 n 作为 N（模式数量）
    - 构造：
        K = 3
        M = n
        P[1..N]：长度为 K 的字符串（'a' + i%3）
        M 条查询 (s, mt)：s 为某个 P[mt]，保证可行解
    """

    import random

    # ---------- 1. 构造测试数据 ----------
    N = n
    if N <= 0:
        return

    K = 3                        # 每个模式的长度
    M = N                        # 给 M 取和 N 同规模

    # 构造 P[1..N]，P[0] 作为占位
    P = [""]
    for i in range(N):
        # 简单可重复的构造：比如 'abc', 'bca', 'cab', ...
        base = ['a', 'b', 'c']
        s = ''.join(base[(i + j) % 3] for j in range(K))
        P.append(s)

    # 构造 p2i 字典
    p2i = {p: i for i, p in enumerate(P)}

    # 构造 M 条 (s, mt)，保证一定存在满足条件的边与 ok=1
    queries = []
    for _ in range(M):
        mt = random.randint(1, N)
        s = P[mt]  # 为保证 ok=1，直接用模式字符串本身
        queries.append((s, mt))

    # ---------- 2. 原算法逻辑（去掉 input，使用上述构造） ----------

    adj = [set() for _ in range(N + 1)]
    for s, mt in queries:
        ok = 0
        for k in range(1 << K):
            s_new = ["_"] * K
            for j in range(K):
                if k >> j & 1:
                    s_new[j] = s[j]
            s_new = "".join(s_new)
            if s_new != P[mt]:
                if s_new in p2i:
                    adj[mt].add(p2i[s_new])
            else:
                ok = 1
        if not ok:
            print("NO")
            return

    in_num = [0] * (N + 1)
    for v in range(1, N + 1):
        for u in adj[v]:
            in_num[u] += 1

    st = [v for v in range(1, N + 1) if in_num[v] == 0]
    ans = []
    while st:
        v = st.pop()
        ans.append(v)
        for u in adj[v]:
            in_num[u] -= 1
            if in_num[u] == 0:
                st.append(u)

    if len(ans) == N:
        print("YES")
        print(*ans)
    else:
        print("NO")


if __name__ == '__main__':
    # 示例：调用 main(5)
    main(5)