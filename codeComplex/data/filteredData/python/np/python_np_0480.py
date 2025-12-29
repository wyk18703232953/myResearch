from collections import deque
import random
import string


def match(s, k):
    res = []
    for i in range(1 << k):
        tmp = []
        for j in range(k):
            if (i >> j) & 1:
                tmp.append(s[j])
            else:
                tmp.append("_")
        res.append("".join(tmp))
    return set(res)


def gen_random_pattern(k):
    # 生成长度为 k 的模式串，由小写字母和 '_' 组成
    chars = string.ascii_lowercase + "_"
    return "".join(random.choice(chars) for _ in range(k))


def main(n):
    # 为了可复现，固定随机种子
    random.seed(0)

    # 规模解释：
    # n: 字符串个数
    # k: 每个模式串的长度（取一个较小值以避免 2^k 过大）
    # m: 查询条数（这里简单设置为 n 的 2 倍）
    k = max(1, min(5, n))  # 防止 2^k 过大，同时保证与 n 有关
    m = max(1, 2 * n)

    # 生成 n 个长度为 k 的模式串 p
    p = []
    seen = set()
    while len(p) < n:
        s = gen_random_pattern(k)
        # 允许有 '_'，但保持唯一性
        if s not in seen:
            seen.add(s)
            p.append(s)

    idx = {s: i for i, s in enumerate(p)}

    # 生成 m 条 (s, mt) 数据
    # s: 查询模式串
    # mt: 目标索引（1-based），对应原代码中的 mt
    queries = []
    for _ in range(m):
        mt = random.randint(1, n)  # 1-based
        base = p[mt - 1]
        # 随机生成一个 s，部分位置来自 base，部分位置随机
        s_list = list(base)
        for pos in range(k):
            if random.random() < 0.5:
                # 替换为随机字符（包括 '_'），制造一定概率失配
                s_list[pos] = random.choice(string.ascii_lowercase + "_")
        s = "".join(s_list)
        queries.append((s, mt))

    # 以下为原逻辑，只是从生成的数据中读取
    edge = [[] for _ in range(n)]
    deg = [0] * n

    for s, mt in queries:
        mt -= 1  # 转为 0-based
        t = p[mt]
        M = match(s, k)
        if t in M:
            for nv in M:
                if nv != t and nv in idx:
                    v_id = idx[nv]
                    edge[mt].append(v_id)
                    deg[v_id] += 1
        else:
            print("NO")
            return

    deq = deque([v for v in range(n) if deg[v] == 0])
    res = []
    while deq:
        v = deq.popleft()
        res.append(v + 1)  # 输出仍为 1-based
        for nv in edge[v]:
            deg[nv] -= 1
            if deg[nv] == 0:
                deq.append(nv)

    if len(res) != n:
        print("NO")
        return

    print("YES")
    print(*res)


if __name__ == "__main__":
    # 示例：可以在此修改 n 测试不同规模
    main(5)