def main(n):
    from collections import Counter

    # 生成确定性输入：n, k, a
    # 设定 k，使得位数随规模变化，但有上限
    k = 20 if n > 20 else max(1, n)
    mask = (1 << k) - 1

    # 生成长度为 n 的数组 a，使用简单确定性构造
    a = [(i * 17 + 23) & mask for i in range(n)]

    # 原始预处理逻辑
    for i in range(n):
        ai = a[i]
        nai = mask ^ ai
        if nai < ai:
            a[i] = nai

    # 原始核心算法逻辑
    C = Counter()
    C[0] += 1
    S = 0
    cnt = 0
    for j, ai in enumerate(a):
        nai = mask ^ ai
        v1, v2 = C[S ^ ai], C[S ^ nai]
        if v1 <= v2:
            cnt += j + 1 - v1
            S ^= ai
            C[S] += 1

        else:
            cnt += j + 1 - v2
            S ^= nai
            C[S] += 1

    # print(cnt)
    pass
if __name__ == "__main__":
    main(10)