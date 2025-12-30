import random
import string


def can_form(s: str, t: str) -> bool:
    n = len(s)
    m = len(t)

    # Build next-position array
    INF = 1000
    pos = [[INF for _ in range(26)] for _ in range(n + 2)]
    for i in range(n, -1, -1):
        if i < n:
            for j in range(26):
                pos[i][j] = pos[i + 1][j]
        if i > 0:
            x = ord(s[i - 1]) - 97
            pos[i][x] = i

    # Try all splits t = t1 + t2
    for i in range(m):
        t1 = t[:i]
        t2 = t[i:]
        m1 = len(t1)
        m2 = len(t2)
        dp = [[INF for _ in range(m2 + 1)] for _ in range(m1 + 1)]
        dp[0][0] = 0

        for j in range(m1 + 1):
            for k in range(m2 + 1):
                if j > 0 and dp[j - 1][k] < INF:
                    t1x = ord(t1[j - 1]) - 97
                    dp[j][k] = min(dp[j][k], pos[dp[j - 1][k] + 1][t1x])
                if k > 0 and dp[j][k - 1] < INF:
                    t2x = ord(t2[k - 1]) - 97
                    dp[j][k] = min(dp[j][k], pos[dp[j][k - 1] + 1][t2x])

        if dp[-1][-1] < INF:
            return True
    return False


def main(n: int):
    """
    n: 规模参数，用于控制测试数据大小和数量。
       这里约定：
       - 测试组数 test = max(1, n // 3)
       - 每个 s, t 的长度在 [1, n] 内随机
    """
    random.seed(0)

    test = max(1, n // 3)
    for _ in range(test):
        len_s = random.randint(1, n)
        len_t = random.randint(1, n)

        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_s))
        t = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_t))

        if can_form(s, t):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    # 示例：规模 n = 10，可按需要修改
    main(10)