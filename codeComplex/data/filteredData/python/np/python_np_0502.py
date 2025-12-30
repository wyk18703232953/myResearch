import collections
import random
import string

def binary(s):
    ans = set()
    for i in range(2 ** len(s)):
        x = []
        for j in range(len(s)):
            if (i >> j) & 1:
                x.append(s[j])
            else:
                x.append('_')
        ans.add(''.join(x))
    return ans


def main(n):
    # ========== 测试数据生成 ==========
    # n: 字符串数量（节点数）
    # 随机生成 m（约为 n 的 1.5 倍）
    m = max(1, n * 3 // 2)
    # 字符串长度 k 固定为 3，字符集为小写字母
    k = 3
    chars = string.ascii_lowercase

    # 生成 n 个不同的模式串（由字母和 '_' 组成）
    patterns = set()
    while len(patterns) < n:
        s = ''.join(random.choice(chars + '_') for _ in range(k))
        patterns.add(s)
    patterns = list(patterns)

    # d[i]: 第 i 个模式串（1-based），dop: 反向映射
    d = {}
    dop = {}
    for i in range(1, n + 1):
        d[i] = patterns[i - 1]
        dop[d[i]] = i

    # 随机生成 m 条约束：字符串 s 和索引 ind
    constraints = []
    for _ in range(m):
        base = random.choice(patterns)
        # 随机修改 base 的部分位置为 '_'
        s_list = list(base)
        for i in range(k):
            if random.random() < 0.5:
                s_list[i] = '_'
        s = ''.join(s_list)

        # 保证 d[ind] 属于 binary(s)，否则原逻辑会立即输出 NO
        s_set = binary(s)
        # 找一个 d[ind] 在 s_set 中的索引
        candidates = [idx for idx in range(1, n + 1) if d[idx] in s_set]
        if not candidates:
            # 若无候选，使得当前约束可行：直接用一个存在的模式
            ind = random.randint(1, n)
            s = d[ind]  # 这样必定满足 d[ind] in binary(s)
        else:
            ind = random.choice(candidates)
        constraints.append((s, ind))

    # ========== 原逻辑部分（移除 input，使用上面生成的数据） ==========
    mod = 10 ** 9 + 7

    seen = set()
    visited = set()
    topo_order = []

    def dfs(i):
        visited.add(i)
        seen.add(i)
        for j in graph[i]:
            if j in visited:
                return True
            if j in seen:
                continue
            if dfs(j):
                return True
        topo_order.append(str(i))
        visited.remove(i)
        return False

    def topo(graph_):
        seen.clear()
        for i in range(1, n + 1):
            if i in seen:
                continue
            if dfs(i):
                return False
        return True

    graph = collections.defaultdict(list)
    for s, ind in constraints:
        sset = binary(s)
        if d[ind] not in sset:
            print('NO')
            return
        for pattern in sset:
            if pattern in dop and dop[pattern] != ind:
                graph[dop[pattern]].append(ind)
    else:
        if topo(graph):
            print('YES')
            print(' '.join(topo_order))
        else:
            print('NO')


if __name__ == "__main__":
    # 示例调用：规模 n 可自行调整
    main(5)