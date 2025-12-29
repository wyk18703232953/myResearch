import random
from collections import deque

def main(n):
    # 参数设计：
    # n: 模式数量
    # k: 模式长度
    # m: 查询数量
    #
    # 随机生成满足基本约束的数据：
    # - P 中有 n 个长度为 k 的模式，由小写字母和 '_' 组成
    # - S 中有 m 条查询 (字符串, 下标)

    random.seed(0)

    # 设定 k 和 m，可根据需要调整生成策略
    k = max(1, min(5, n))        # k 不宜太大，否则 2^k 暴涨
    m = max(1, n)                # 让 m 与 n 同阶

    # 生成 P：随机由 [a,b,c] 和 '_' 构成的长度为 k 的字符串（可自行调整字符集）
    alphabet = ['a', 'b', 'c', '_']
    P = []
    for _ in range(n):
        s = ''.join(random.choice(alphabet) for _ in range(k))
        P.append(s)

    # 为了提高测试有效性，构造 S 时尽量保证存在匹配
    # 构造方式：
    #   对于每个查询，随机选一个 P[i]，将其作为 x 的「模板」，
    #   然后将其中的 '_' 替换成随机字母，得到具体字符串 x，
    #   并令该查询指向 i（即保证至少有一个合法匹配）。
    S = []
    for _ in range(m):
        idx = random.randrange(n)
        pat = P[idx]
        x_chars = []
        for ch in pat:
            if ch == '_':
                x_chars.append(random.choice(['a', 'b', 'c']))
            else:
                x_chars.append(ch)
        x = ''.join(x_chars)
        S.append([x, idx + 1])  # 原代码中读入时是 1-based，再减一

    # ===== 以下为原始逻辑（去掉 input），封装为 main(n) 内部 =====

    # 将 S[i][1] 变为 0-based
    for i in range(m):
        S[i][1] = int(S[i][1]) - 1

    # 建立模式到索引的字典
    PDICT = {}
    for i in range(n):
        PDICT[P[i]] = i

    E = []  # 边集

    for i in range(m):
        x = S[i][0]
        LIST = []

        # 枚举所有掩码，将 x 的若干位替换成 '_' 后，查看是否在 PDICT 中
        for j in range(1 << k):
            t = []
            for l in range(k):
                if (1 << l) & j != 0:
                    t.append("_")
                else:
                    t.append(x[l])
            t = "".join(t)

            if t in PDICT:
                LIST.append(PDICT[t])

        # 检查目标索引是否在 LIST 中
        if S[i][1] not in LIST:
            print("NO")
            return
        else:
            s = S[i][1]
            for l in LIST:
                if l == s:
                    continue
                else:
                    E.append((s, l))

    # 建图并进行拓扑排序
    EDGEIN = [0] * n
    EDGEOUTLIST = [[] for _ in range(n)]
    for x, y in E:
        EDGEIN[y] += 1
        EDGEOUTLIST[x].append(y)

    que = deque()

    for i in range(n):
        if EDGEIN[i] == 0:
            que.append(i)

    top_sort = []
    while que:
        x = que.pop()
        top_sort.append(x)
        for to in EDGEOUTLIST[x]:
            EDGEIN[to] -= 1
            if EDGEIN[to] == 0:
                que.appendleft(to)

    if len(top_sort) == n:
        print("YES")
        print(*[i + 1 for i in top_sort])
    else:
        print("NO")


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)