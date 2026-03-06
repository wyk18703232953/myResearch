import math

mod = 998244353
INF = float('inf')


def cord(c):
    return ord(c) - ord('a')


def main(n):
    # 定义规模：
    # m = min(12, max(1, n // 5))
    # n_char = max(n, m + 1)  保证至少有 2 个字符
    m = min(12, max(1, n // 5))
    n_char = max(n, m + 1)

    # 生成确定性的 n, m, s
    # 字符串由前 m 个字母周期性重复构造
    s = ''.join(chr(ord('a') + (i % m)) for i in range(n_char))

    ct = [0] * (1 << m)

    for i in range(n_char - 1):
        now, nex = cord(s[i]), cord(s[i + 1])
        if now == nex:
            continue
        ct[(1 << now) | (1 << nex)] += 1

    for i in range(m):
        for j in range(1 << m):
            if (1 << i) & j:
                ct[j] += ct[(1 << i) ^ j]

    dp = [INF] * (1 << m)
    dp[0] = 0
    full_mask = (1 << m) - 1

    for i in range(1 << m):
        for j in range(m):
            if i & (1 << j) == 0:
                # 使用原代码中的位运算形式：
                # sm = ct[-1] - ct[i] - ct[~i]
                # 这里 ct[-1] 对应 ct[full_mask]，ct[~i] 需要限制到 m 位
                sm = ct[full_mask] - ct[i] - ct[(~i) & full_mask]
                nxt = i | (1 << j)
                if dp[nxt] > dp[i] + sm:
                    dp[nxt] = dp[i] + sm

    print(dp[full_mask])


if __name__ == "__main__":
    main(20)