import sys
from collections import defaultdict as dft

def main(n):
    # n 作为词汇数量，同时也是模式长度 k
    # 构造参数
    k = max(1, n // 2)
    m = n  # 查询数量与词数相同

    # 构造 n 个长度为 k 的单词，字符为 'a'..'z' 和 '_' 的确定性组合
    chars = [chr(ord('a') + (i % 26)) for i in range(k)]
    iput = []
    for i in range(n):
        # 每个单词第 j 位为 chars[(i + j) % len(chars)]
        word = "".join(chars[(i + j) % len(chars)] for j in range(k))
        iput.append(word)

    # 构造字典 dct
    dct = {}
    for i, word in enumerate(iput, start=1):
        dct[word] = i

    # 构造 m 个查询 (word, idx)
    # 这里生成的 word 由 iput[idx-1] 派生，按位决定是否变为 '_'
    queries = []
    for q in range(m):
        idx = (q % n) + 1
        base = iput[idx - 1]
        # 确定性地构造 word：第 j 位，如果 (q+j) 为偶数则 '_', 否则复制 base[j]
        word = "".join('_' if ((q + j) % 3 == 0) else base[j] for j in range(k))
        queries.append((word, idx))

    # 原算法逻辑开始
    d = [[] for _ in range(n + 1)]
    size = [0] * (n + 1)

    for (word, idx) in queries:
        temp = 1
        w = iput[idx - 1]

        for x in range(k):
            if w[x] != '_' and w[x] != word[x]:
                temp = 0
                print("NO")
                return

        res = []
        for mask in range(1 << k):
            s = "".join([word[x] if (mask & (1 << x)) == 0 else '_' for x in range(k)])
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
    # 示例调用，可根据需要修改 n 的规模
    main(5)