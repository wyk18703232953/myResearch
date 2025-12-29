import random

INF = 10**9


def main(n: int) -> int:
    """
    n: length of the generated string
    返回值: 原程序最终的 dp[-1] 结果
    """

    # 设定字符种类数 m（可按需要调整，这里给一个例子：不超过 20）
    m = min(20, max(1, n if n > 0 else 1))

    # 随机生成长度为 n、字母种类为前 m 个小写字母的字符串 s
    # 为避免所有相邻字符都相同导致信息过少，这里简单随机生成
    alphabet = [chr(ord('a') + i) for i in range(m)]
    s = "".join(random.choice(alphabet) for _ in range(n))

    # 以下为原逻辑（去掉 input 部分）
    adj_in_subset = [0] * (1 << m)
    ord_a = ord("a")

    for c1, c2 in zip(s, s[1:]):
        c1 = ord(c1) - ord_a
        c2 = ord(c2) - ord_a
        if c1 != c2:
            adj_in_subset[(1 << c1) + (1 << c2)] += 1

    for i in range(m):
        for j in range(1 << m):
            if j & (1 << i):
                adj_in_subset[j] += adj_in_subset[j ^ (1 << i)]

    total_adj = adj_in_subset[-1]
    dp = [INF] * (1 << m)
    dp[0] = 0

    full_mask = (1 << m) - 1
    for i in range(1 << m):
        for j in range(m):
            if i & (1 << j):
                continue
            # Python 中 ~i 是按无限位取反，需与 full_mask 与一下以限制在 m 位
            cost = total_adj - adj_in_subset[i] - adj_in_subset[(~i) & full_mask]
            ni = i | (1 << j)
            if dp[ni] > dp[i] + cost:
                dp[ni] = dp[i] + cost

    # 输出与原程序一致
    print(dp[-1])
    return dp[-1]


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)