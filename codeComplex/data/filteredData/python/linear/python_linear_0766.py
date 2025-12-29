import random

def main(n):
    # 生成测试数据
    # n 为数组长度，q 为查询次数
    # 这里设定 q = n，且 ai 为 1..n 的随机排列
    q = n
    ai = list(range(1, n + 1))
    random.shuffle(ai)

    # 原始逻辑开始
    ar = []
    ar3 = []
    num = 1
    nummm = max(ai)
    if ai[0] != nummm:
        num2 = ai[0]
        for i in range(1, n):
            ar3 += [[num2, ai[i]]]
            if ai[i] == nummm:
                ar += [num2]
                num = i + 1
                break
            if ai[i] > num2:
                ar += [num2]
                num2 = ai[i]
            else:
                ar += [ai[i]]

    ar2 = []
    for i in range(num, n):
        ar2 += [ai[i]]
    for i in range(len(ar)):
        ar2 += [ar[i]]

    num_pairs = len(ar3)

    # 构造 q 个查询 m（例如 1..q）
    queries = list(range(1, q + 1))

    # 输出对应的答案
    for m in queries:
        if m <= num_pairs:
            print(ar3[m - 1][0], ar3[m - 1][1])
        else:
            m_adj = m - num_pairs - 1
            print(nummm, ar2[m_adj % (n - 1)])


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)