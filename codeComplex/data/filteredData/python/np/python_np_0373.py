def main(n):
    import sys
    sys.setrecursionlimit(10**7)

    INF = 10**9

    # 映射 n -> (字符串长度, 字母种类数)
    # 保证 m 至少为 1，至多为 20（因为依赖 2^m）
    # 让 m 随 n 缓慢增长，方便规模实验
    if n <= 0:
        n = 1
    m = min(20, max(1, n % 20 + 1))
    length = n

    # 确定性构造字符串 s，使用前 m 个小写字母周期性生成
    # s 的长度为 length
    alphabet = [chr(ord('a') + i) for i in range(m)]
    s = ''.join(alphabet[i % m] for i in range(length))

    count = [[0] * m for _ in range(m)]
    ord_a = ord("a")
    for c1, c2 in zip(s, s[1:]):
        c1 = ord(c1) - ord_a
        c2 = ord(c2) - ord_a
        if c1 != c2:
            count[c1][c2] += 1

    sum_of_subset = [[0] * (1 << m) for _ in range(m)]
    for i in range(m):
        for j in range(1 << m):
            if j == 0:
                continue
            lsb = j & -j
            sum_of_subset[i][j] = sum_of_subset[i][j ^ lsb] + count[i][lsb.bit_length() - 1]

    adj_in_subset = [0] * (1 << m)
    for i in range(1 << m):
        total = 0
        for j in range(m):
            if i & (1 << j):
                total += sum_of_subset[j][i]
        adj_in_subset[i] = total

    total_adj = adj_in_subset[-1]
    dp = [INF] * (1 << m)
    dp[0] = 0

    full_mask = (1 << m) - 1
    for i in range(1 << m):
        for j in range(m):
            if i & (1 << j):
                continue
            # Python 中负数按无限位补码处理，这里保持原逻辑使用 ~i
            cost = total_adj - adj_in_subset[i] - adj_in_subset[~i & full_mask]
            ni = i | (1 << j)
            new_val = dp[i] + cost
            if new_val < dp[ni]:
                dp[ni] = new_val

    print(dp[-1])


if __name__ == "__main__":
    main(10)