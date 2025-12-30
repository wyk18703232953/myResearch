import random
import string
from collections import defaultdict

def solve_instance(n, m, k, words, queries):
    # Original solve() core, but without input() and exit()
    dct = {}
    iput = []
    for i in range(n):
        word = words[i]
        dct[word] = i + 1
        iput.append(word)

    d = [[] for _ in range(n + 1)]
    size = [0] * (n + 1)

    for (word, idx) in queries:
        temp = 1
        w = iput[idx - 1]

        for x in range(k):
            if w[x] != '_' and w[x] != word[x]:
                temp = 0
                return "NO\n"  # early failure like original exit()

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
        return "YES\n" + " ".join(map(str, st)) + "\n"
    else:
        return "NO\n"


def generate_test_data(n):
    """
    根据规模 n 生成一组 (n, m, k, words, queries)

    约定：
    - 令 k = min(5, max(1, n))，保证单词长度不大且 >=1
    - 生成 n 个互不相同的单词，字母表为小写英文字母
    - 生成 m = n 条查询，每条查询的 word 由原单词随机改若干位为 '_'
      以及再随机改若干位为其他字母，保证与原 solve 的约束兼容。
    """
    # 选择 k（单词长度）
    k = min(5, max(1, n))

    # 生成 n 个不同的单词
    words_set = set()
    alph = string.ascii_lowercase
    while len(words_set) < n:
        w = ''.join(random.choice(alph) for _ in range(k))
        words_set.add(w)
    words = list(words_set)

    # 生成 m 条查询，这里取 m = n
    m = n
    queries = []
    for idx in range(1, n + 1):
        base = words[idx - 1]
        w_list = list(base)

        # 随机把一些位置改成 '_'，保证至少一个位置不变
        positions = list(range(k))
        random.shuffle(positions)
        num_underscore = random.randint(0, k - 1)
        for p in positions[:num_underscore]:
            w_list[p] = '_'

        # 再随机改一些非 '_' 位置为其他字符（可为 0 个）
        non_underscore_pos = [i for i in range(k) if w_list[i] != '_']
        change_cnt = random.randint(0, max(0, len(non_underscore_pos) - 1))
        random.shuffle(non_underscore_pos)
        for p in non_underscore_pos[:change_cnt]:
            orig = w_list[p]
            cand = random.choice([c for c in alph if c != orig])
            w_list[p] = cand

        query_word = ''.join(w_list)
        queries.append((query_word, idx))

    return n, m, k, words, queries


def main(n):
    """
    封装逻辑的入口函数：
    - n 为规模参数
    - 自动生成测试数据
    - 调用改写后的 solve 逻辑
    - 将结果输出到标准输出
    """
    n, m, k, words, queries = generate_test_data(n)
    result = solve_instance(n, m, k, words, queries)
    print(result, end='')


if __name__ == "__main__":
    # 示例：可自行修改 n 测试
    main(5)