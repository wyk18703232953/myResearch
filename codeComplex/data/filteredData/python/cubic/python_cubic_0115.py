import random
import string

INF = 1e20


def solve(s1, s2, nxt):
    # i => s1, j => s2
    dp = [[INF for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    dp[0][0] = 0
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if dp[i][j] == INF:
                continue

            if i < len(s1) and dp[i][j] < len(nxt) and nxt[int(dp[i][j])][ord(s1[i]) - ord('a')] < INF:
                dp[i + 1][j] = min(dp[i + 1][j], nxt[int(dp[i][j])][ord(s1[i]) - ord('a')] + 1)
            if j < len(s2) and dp[i][j] < len(nxt) and nxt[int(dp[i][j])][ord(s2[j]) - ord('a')] < INF:
                dp[i][j + 1] = min(dp[i][j + 1], nxt[int(dp[i][j])][ord(s2[j]) - ord('a')] + 1)

    return dp[len(s1)][len(s2)]


def main(n: int):
    """
    n: 规模参数，用于决定测试数据大小和测试组数。
       这里约定：
       - T = n（测试组数）
       - 每个 s 的长度为 n
       - 每个 rs 的长度为 n
    """
    T = n

    for _ in range(T):
        # 生成测试串 s 和 rs，仅包含小写字母
        s_len = n
        rs_len = n
        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(s_len))
        rs = ''.join(random.choice(string.ascii_lowercase) for _ in range(rs_len))

        nxt = [[INF for _ in range(26)] for _ in range(len(s))]

        # 预处理 next 数组
        for i in range(len(s) - 1, -1, -1):
            if i < len(s) - 1:
                for j in range(26):
                    nxt[i][j] = nxt[i + 1][j]
            nxt[i][ord(s[i]) - ord('a')] = i

        found = False

        if len(rs) == 1:
            if rs in s:
                found = True
        else:
            for p in range(1, len(rs)):
                s1 = rs[:p]
                s2 = rs[p:]

                if solve(s1, s2, nxt) < INF:
                    found = True
                    break

        if found:
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)