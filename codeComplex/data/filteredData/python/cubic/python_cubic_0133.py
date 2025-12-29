import random
import string


def solve_one(s: str, t: str) -> str:
    # convert chars to 0-25
    s_arr = [ord(c) - 97 for c in s]
    t_arr = [ord(c) - 97 for c in t]
    n, m = len(s_arr), len(t_arr)

    # nxt[i][c]: from position i, first index >= i where s[index] == c, or n+1
    nxt = [[n + 1] * 26 for _ in range(n + 2)]
    for i in range(n - 1, -1, -1):
        nxt[i] = nxt[i + 1][:]
        nxt[i][s_arr[i]] = i

    for b in range(m + 1):
        t1 = t_arr[:b]
        t2 = t_arr[b:]
        len1 = b
        len2 = m - b

        # dp[j][k]: smallest index in s reachable after matching
        # first j chars of t1 and first k chars of t2 in order (interleaved),
        # or n+1 if impossible
        dp = [[n + 1] * (len2 + 1) for _ in range(len1 + 1)]
        dp[0][0] = 0

        for j in range(len1 + 1):
            for k in range(len2 + 1):
                if j:
                    idx = dp[j - 1][k]
                    if idx <= n:
                        dp[j][k] = min(dp[j][k], nxt[idx][t1[j - 1]] + 1)
                if k:
                    idx = dp[j][k - 1]
                    if idx <= n:
                        dp[j][k] = min(dp[j][k], nxt[idx][t2[k - 1]] + 1)

        if dp[len1][len2] <= n:
            return 'YES'
    return 'NO'


def main(n: int):
    """
    生成规模由 n 控制的随机测试数据并执行原逻辑。

    约定：
    - 生成 T = n 个测试用例（可按需要调整）
    - 对每个测试：
        len(s) 在 [1, n]
        len(t) 在 [1, n]
        s, t 为小写字母随机串
    """
    random.seed(0)

    T = n
    for _ in range(T):
        len_s = random.randint(1, n)
        len_t = random.randint(1, n)
        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_s))
        t = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_t))
        print(s, t, solve_one(s, t))


if __name__ == "__main__":
    # 示例：n=5 时生成 5 组随机测试
    main(5)