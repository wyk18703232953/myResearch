def main(n):
    # 确定性生成输入规模 n, 位数 k，以及数组 a
    # 这里令 k = max(1, n.bit_length())，保证位数随规模增长
    k = max(1, n.bit_length())
    # 生成长度为 n 的数组 a，元素为 [i ^ (i // 2)] & ((1<<k) - 1)
    mask = (1 << k) - 1
    a = [((i ^ (i // 2)) & mask) for i in range(n)]

    # 保持原算法逻辑
    for i in range(n):
        ai = a[i]
        nai = mask ^ ai
        if nai < ai:
            a[i] = nai

    from collections import Counter
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