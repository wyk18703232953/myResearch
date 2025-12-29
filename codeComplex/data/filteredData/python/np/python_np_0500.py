def main(n):
    import random

    # -----------------------------
    # 1. 根据规模 n 生成测试数据
    # -----------------------------
    # 约定：
    #   N = n             模式串数量
    #   K = 3             模式长度（可改大，但需保证 2^K 不过大）
    #   M = n             查询数量
    #
    # 字符串字符集：'a', 'b', 'c', '_'(只在查询中出现)
    #
    # 原程序输入格式：
    #   N M K
    #   N 行模式串（每行长度 K，且不含 '_'）
    #   M 行：query_string index
    #
    # 为保证有解，先构造一个简单的拓扑序，然后保证查询不与模式冲突。

    K = 3
    N = n
    M = n

    letters = ['a', 'b', 'c']

    # 生成 N 个不同的模式串（仅 a,b,c）
    # 若 N > 3^K，无法保证互异，这里简单截断
    all_patterns = []
    def gen_all_patterns(cur):
        if len(cur) == K:
            all_patterns.append(''.join(cur))
            return
        for ch in letters:
            cur.append(ch)
            gen_all_patterns(cur)
            cur.pop()

    gen_all_patterns([])
    if N > len(all_patterns):
        N = len(all_patterns)  # 截断
        M = N

    S = all_patterns[:N]

    # 随机生成 M 个查询：
    # 查询形式：Q_str idx
    # Q_str 在原题要求是长度 K，可以包含 '_'。
    # 同时必须满足：若 Q_str 与 S[idx] 冲突，则原程序会直接 NO 退出。
    # 为避免这种情况，生成时强制与 S[idx] 不冲突。
    T = []  # (Q_str, idx)
    for _ in range(M):
        idx = random.randrange(0, N)
        base = S[idx]
        q_chars = []
        for j in range(K):
            # 以一定概率放 '_', 否则放与 base 相同字符（保证不冲突）
            if random.random() < 0.5:
                q_chars.append('_')
            else:
                q_chars.append(base[j])
        Q_str = ''.join(q_chars)
        # 保证与 S[idx] 不冲突：只要在非 '_' 位置字符相等即可
        # 上面构造方式已经满足，不额外检查
        T.append([Q_str, idx])

    # -----------------------------
    # 2. 把原逻辑封装为函数，直接使用生成的数据
    # -----------------------------

    # 构造映射 D
    D = {S[i]: i for i in range(N)}

    # 原始 T 中第二列是 0-based index，无需减 1
    G = [[] for _ in range(N)]
    C = [0] * N

    for i in range(M):
        q_str, idx = T[i]

        # 检查是否与模式冲突
        for j in range(K):
            if S[idx][j] != '_' and S[idx][j] != q_str[j]:
                print('NO')
                return

        # 枚举所有子掩码，把非选中的位置替换成 '_'
        for mask in range(1 << K):
            t = ''.join(['_' if (mask & (1 << k)) else q_str[k] for k in range(K)])
            x = D.get(t, -1)
            if x != -1 and x != idx:
                G[idx].append(x)
                C[x] += 1

    P = []
    Q = []
    F = [1] * N

    for i in range(N):
        if C[i] == 0 and F[i]:
            Q.append(i)
        while Q:
            v = Q.pop()
            if not F[v]:
                continue
            F[v] = 0
            P.append(v + 1)
            for to in G[v]:
                C[to] -= 1
                if C[to] == 0:
                    Q.append(to)

    if len(P) == N:
        print('YES')
        print(*P)
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：n = 5
    main(5)