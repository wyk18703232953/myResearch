from random import randint, choice
from string import ascii_lowercase


def patterns(s):
    if len(s) == 1:
        return [s, '_']
    else:
        tp = patterns(s[1:])
        return [s[0] + t for t in tp] + ['_' + t for t in tp]


def solve(n, patterns_list, queries):
    ppm = {}
    for i, p in enumerate(patterns_list):
        ppm[p] = i

    pre = [0] * n
    suc = [[] for _ in range(n)]

    for s, ml in queries:
        ml -= 1
        ps = patterns(s)
        found = False
        for p in ps:
            if p in ppm:
                if ppm[p] == ml:
                    found = True
                else:
                    pre[ppm[p]] += 1
                    suc[ml].append(ppm[p])
        if not found:
            print("NO")
            return

    znodes = [i for i in range(n) if pre[i] == 0]
    res = []
    while znodes:
        i = znodes.pop()
        res.append(i + 1)
        for j in suc[i]:
            pre[j] -= 1
            if pre[j] == 0:
                znodes.append(j)

    if len(res) == n:
        print("YES")
        print(' '.join(map(str, res)))
    else:
        print("NO")


def gen_pattern_string(length, alphabet_size=3):
    alphabet = ascii_lowercase[:alphabet_size]
    return ''.join(choice(alphabet) for _ in range(length))


def main(n):
    # 规模 n 为模式数量
    # 随机生成模式串和查询
    # 为了保持可控，长度和查询数量与 n 挂钩
    max_len = max(1, min(5, n))          # 模式最大长度
    m = max(1, n * 2)                    # 查询数量
    k = max_len                          # 保留原代码中的 k 语义（最大长度）

    # 生成 n 个不同的模式串（可能包含 '_'）
    patterns_set = set()
    patterns_list = []
    while len(patterns_list) < n:
        L = randint(1, max_len)
        s = gen_pattern_string(L)
        # 随机用 '_' 替换若干字符得到模式
        s_list = list(s)
        for i in range(L):
            if randint(0, 3) == 0:       # 1/4 机会变成通配符
                s_list[i] = '_'
        pat = ''.join(s_list)
        if pat not in patterns_set:
            patterns_set.add(pat)
            patterns_list.append(pat)

    # 生成 m 个查询：
    # 其中部分保证有匹配，部分随机
    queries = []
    for _ in range(m):
        if randint(0, 1) == 0:
            # 构造一定能匹配的查询：从某个模式反推一个具体串
            idx = randint(0, n - 1)
            pat = patterns_list[idx]
            s_list = []
            for ch in pat:
                if ch == '_':
                    s_list.append(choice(ascii_lowercase[:3]))
                else:
                    s_list.append(ch)
            s = ''.join(s_list)
            # 对应的 ml 设成 idx+1，保证存在匹配
            queries.append((s, idx + 1))
        else:
            # 随机生成查询（不保证匹配）
            L = randint(1, max_len)
            s = gen_pattern_string(L)
            ml = randint(1, n)
            queries.append((s, ml))

    # 调用原逻辑
    # 原 main 的输入形态是：n, m, k 但 k 实际没有参与逻辑
    # 这里只在生成过程中使用，solve 不再需要 k
    solve(n, patterns_list, queries)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)