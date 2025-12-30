import random


def main(n: int):
    # 生成测试数据
    # N: 模式数量, K: 模式长度, M: 查询数量
    N = n
    K = max(1, n // 3)          # 控制模式长度
    M = max(1, n * 2)           # 控制查询数

    # 随机生成 N 个长度为 K 的模式字符串，只含小写字母和 '_'
    # 原题中通常 '_' 也可能在模式中，因此保留
    alphabet = "abc"            # 控制字符种类，便于出现匹配关系
    patterns = []
    D_P = {}

    for i in range(N):
        s = "".join(random.choice(alphabet + "_") for _ in range(K))
        patterns.append(s)
        D_P[s] = i

    # 生成 M 个查询 (S, mt)
    # S: 模式字符串，mt: 1-based index of pattern to match
    queries = []
    for _ in range(M):
        mt = random.randint(1, N)   # 1-based
        base = patterns[mt - 1]

        # 基于 base 生成一个 S，使得 base 可以匹配 S 或不匹配 S
        # 随机决定是否强制可匹配
        force_match = random.choice([True, False])

        s_list = list(base)
        for i in range(K):
            if force_match:
                # 使 base[i] ∈ {S[i], '_'}
                if random.random() < 0.5:
                    s_list[i] = base[i] if base[i] != "_" else random.choice(alphabet)
                else:
                    s_list[i] = base[i]
            else:
                # 有概率故意破坏匹配条件
                if random.random() < 0.3:
                    # 把这个位置改成与 base[i] 冲突的字符
                    c_choices = alphabet
                    if base[i] in alphabet:
                        c_choices = "".join(c for c in alphabet if c != base[i])
                    if c_choices:
                        s_list[i] = random.choice(c_choices)
                    else:
                        s_list[i] = random.choice(alphabet)
                else:
                    s_list[i] = base[i] if base[i] != "_" else random.choice(alphabet)

        S = "".join(s_list)
        queries.append((S, mt))

    # 将原逻辑封装，并在生成的数据上运行
    P = patterns
    adj = [[] for _ in range(N)]
    indeg = [0] * N

    for S, mt in queries:
        mt = mt - 1  # 转为0-based

        fp = P[mt]

        # 检查 fp 是否可以匹配 S
        if any(fp[i] not in (S[i], '_') for i in range(K)):
            print('NO')
            return

        # 枚举所有模式
        for bs in range(1 << K):
            pat_chars = []
            for i in range(K):
                if bs & (1 << i) == 0:
                    pat_chars.append(S[i])
                else:
                    pat_chars.append('_')
            pat = ''.join(pat_chars)

            if pat == fp:
                continue
            if pat in D_P:
                j = D_P[pat]
                indeg[j] += 1
                adj[mt].append(j)

    # 拓扑排序
    Q = [i for i in range(N) if indeg[i] == 0]
    for i in Q:
        for j in adj[i]:
            indeg[j] -= 1
            if indeg[j] == 0:
                Q.append(j)

    if len(Q) == N:
        print('YES')
        print(' '.join(str(v + 1) for v in Q))
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)