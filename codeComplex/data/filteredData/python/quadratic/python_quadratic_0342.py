from collections import Counter
import random
import string


def main(n: int):
    # 1. 生成测试数据：随机字符串 s，打乱得到 t（保证可行）
    # 字符集为小写字母
    letters = string.ascii_lowercase

    # 生成随机字符串 s
    s = [random.choice(letters) for _ in range(n)]

    # 为保证 s 和 t 具有相同字符计数，这里直接对 s 的下标做随机排列
    indices = list(range(n))
    random.shuffle(indices)

    # 构造 t，使得 t 是 s 的一个重排
    t = [None] * n
    for i, j in enumerate(indices):
        t[i] = s[j]

    # ------- 以下是原逻辑 -------
    cs = Counter(s)
    ct = Counter(t)
    if cs != ct:
        print(-1)
        return

    xs = [[] for _ in range(26)]
    xt = [[] for _ in range(26)]

    for i in range(n):
        j = ord(s[i]) - ord('a')
        xs[j].append(i)

    for i in range(n):
        j = ord(t[i]) - ord('a')
        xt[j].append(i)

    x = [-1] * n
    for i in range(26):
        for j, k in zip(xs[i], xt[i]):
            x[j] = k

    ans = []
    for i in range(n):
        for j in reversed(range(i + 1, n)):
            if x[j - 1] > x[j]:
                x[j - 1], x[j] = x[j], x[j - 1]
                ans.append(j)

    print(len(ans))
    if ans:
        print(*ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)