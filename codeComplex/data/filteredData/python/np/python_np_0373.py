import sys
sys.setrecursionlimit(10**7)

INF = 10**9

def main(n):
    # 生成规模为 n 的测试数据
    # 约定：m 为字母种类数，固定为 5（可按需修改）
    # s 为长度为 n 的字符串，使用前 m 个小写字母循环构造
    m = 5
    if m > n:
        m = max(1, n)  # 保证 m 不大于 n 且至少为 1

    # 构造一个长度为 n 的字符串 s
    # s 中的字符在前 m 个字母之间循环
    chars = [chr(ord('a') + i) for i in range(m)]
    s_list = [chars[i % m] for i in range(n)]
    s = "".join(s_list)

    # 原始逻辑开始
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
        for j in range(m):
            if i & (1 << j):
                adj_in_subset[i] += sum_of_subset[j][i]

    total_adj = adj_in_subset[-1]
    dp = [INF] * (1 << m)
    dp[0] = 0

    full_mask = (1 << m) - 1
    for i in range(1 << m):
        for j in range(m):
            if i & (1 << j):
                continue
            # 由于 ~i 在 Python 中是按无限位补码表示，需要与 full_mask 取交
            complement = (~i) & full_mask
            cost = total_adj - adj_in_subset[i] - adj_in_subset[complement]
            ni = i | (1 << j)
            if dp[ni] > dp[i] + cost:
                dp[ni] = dp[i] + cost

    # print(dp[-1])
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改 n
    main(10)