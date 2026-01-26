def main(n):
    if n < 2:
        n = 2
    # 构造确定性的 n, q, ai
    q = n
    ai = [(i * 2 + 1) % (3 * n + 7) + 1 for i in range(n)]

    ar = []
    ar3 = []
    num = 1
    nummm = max(ai)
    if ai[0] != nummm:
        num2 = ai[0]
        for i in range(1, n):
            ar3.append([num2, ai[i]])
            if ai[i] == nummm:
                ar.append(num2)
                num = i + 1
                break
            if ai[i] > num2:
                ar.append(num2)
                num2 = ai[i]

            else:
                ar.append(ai[i])
    ar2 = []
    for i in range(num, n):
        ar2.append(ai[i])
    for i in range(len(ar)):
        ar2.append(ar[i])
    num_pairs = len(ar3)

    # 构造确定性的 q 次查询，原程序为 1-based 的 m
    queries = [i + 1 for i in range(q)]

    outputs = []
    for m in queries:
        if m <= num_pairs:
            outputs.append((ar3[m - 1][0], ar3[m - 1][1]))

        else:
            m2 = m - num_pairs - 1
            outputs.append((nummm, ar2[m2 % (n - 1)]))

    for x, y in outputs:
        # print(x, y)
        pass
if __name__ == "__main__":
    main(10)