def main(n):
    # 生成确定性输入数据
    # n 作为数组长度，同时也作为查询数量
    if n <= 0:
        return

    # 原始数组 aa：长度为 n，元素为 i ^ (i // 2)，确保有变化且确定
    aa = [i ^ (i // 2) for i in range(1, n + 1)]

    # 构造 dp，与原逻辑一致
    dp = [aa]
    aa_cur = aa
    for i in range(n - 1, 0, -1):
        aa_tmp = aa_cur[:]
        for j in range(i):
            aa_tmp[j] ^= aa_tmp[j + 1]
        del aa_tmp[-1]
        dp.append(aa_tmp)
        aa_cur = aa_tmp

    # 第二段 dp 处理，与原逻辑一致
    aa2 = dp[0]
    for i, bb in enumerate(dp[1:], 1):
        a = aa2[0]
        for j, b in enumerate(bb):
            c = aa2[j + 1]
            bb[j] = max(a, b, c)
            a = c
        aa2 = bb

    # 构造确定性查询：
    # 生成 n 个区间 [lo, hi]，1 <= lo <= hi <= n
    # 使用简单算术生成多样化区间
    queries = []
    for i in range(1, n + 1):
        lo = (i % n) + 1
        hi = ((i * 2) % n) + 1
        if lo > hi:
            lo, hi = hi, lo
        queries.append((lo, hi))

    # 处理查询并输出结果
    out = []
    for lo, hi in queries:
        out.append(str(dp[hi - lo][lo - 1]))
    # print("\n".join(out))
    pass
if __name__ == "__main__":
    main(5)