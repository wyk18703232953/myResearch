from collections import defaultdict
import random
import string

def main(n):
    # 生成测试数据
    # 固定模式长度 k，生成 n 个模式，以及 m 个查询
    k = 3  # 可以根据需要调整，或设为其他函数参数
    m = n  # 这里简单设定 m = n

    # 生成 n 个长度为 k 的模式串，只含小写字母和 '_'，保证无重复
    patterns = set()
    while len(patterns) < n:
        s = ''.join(random.choice(string.ascii_lowercase + '_') for _ in range(k))
        patterns.add(s)
    patterns = list(patterns)

    # 构造映射：模式串 -> 索引(1-based)
    dct = {word: i + 1 for i, word in enumerate(patterns)}
    iput = patterns[:]  # 原代码中存储输入的数组

    # 生成 m 个查询 (word, idx)
    # 为保证有一定合理性，随机选一个已有模式作为基础，再随机替换一些位
    queries = []
    for _ in range(m):
        idx = random.randint(1, n)
        base = list(iput[idx - 1])
        new_word = base[:]
        for pos in range(k):
            # 以一定概率改变该位置字符
            if random.random() < 0.5:
                new_word[pos] = random.choice(string.ascii_lowercase + '_')
        queries.append(("".join(new_word), idx))

    # 以下是原逻辑移植（去掉 input/exit），使用上面生成的数据
    d = [[] for _ in range(n + 1)]
    size = [0] * (n + 1)

    for word, idx in queries:
        temp = 1
        w = iput[idx - 1]

        for x in range(k):
            if w[x] != '_' and w[x] != word[x]:
                temp = 0
                print("NO")
                return

        for mask in range(1 << k):
            s = "".join(
                word[x] if (mask & (1 << x)) == 0 else '_'
                for x in range(k)
            )
            if s in dct:
                j = dct[s]
                if j != idx:
                    d[idx].append(j)
                    size[j] += 1

    st = [nd for nd in range(1, n + 1) if size[nd] == 0]

    for i in st:
        for j in d[i]:
            size[j] -= 1
            if size[j] == 0:
                st.append(j)

    if len(st) == n:
        print("YES")
        print(*st)
    else:
        print("NO")


if __name__ == "__main__":
    # 示例调用
    main(5)