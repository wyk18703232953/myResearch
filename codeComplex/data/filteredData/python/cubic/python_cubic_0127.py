import random
import string


def solve_case(s: str, t: str) -> str:
    if len(t) == 1:
        return "YES" if t in s else "NO"

    # build nxt array
    nxt = [[-1] * 26 for _ in range(len(s) + 1)]
    nxt[-2][ord(s[-1]) - ord('a')] = len(s) - 1
    for i in range(len(s) - 2, -1, -1):
        for c in range(26):
            nxt[i][c] = nxt[i + 1][c]
        nxt[i][ord(s[i]) - ord('a')] = i

    ans = "NO"
    for p in range(1, len(t)):
        a = t[:p]
        b = t[p:]
        dp = [[-1] * (len(b) + 1) for _ in range(len(a) + 1)]
        dp[0][0] = 0
        for la in range(len(a) + 1):
            for lb in range(len(b) + 1):
                if dp[la][lb] != -1:
                    if la < len(a):
                        idx = nxt[dp[la][lb]][ord(a[la]) - ord('a')]
                        if dp[la + 1][lb] != -1:
                            if idx != -1 and idx < dp[la + 1][lb] - 1:
                                dp[la + 1][lb] = idx
                                dp[la + 1][lb] += 1 + min(0, dp[la + 1][lb])
                        else:
                            dp[la + 1][lb] = idx
                            if dp[la + 1][lb] != -1:
                                dp[la + 1][lb] += 1 + min(0, dp[la + 1][lb])

                    if lb < len(b):
                        idx = nxt[dp[la][lb]][ord(b[lb]) - ord('a')]
                        if dp[la][lb + 1] != -1:
                            if idx != -1 and idx < dp[la][lb + 1] - 1:
                                dp[la][lb + 1] = idx
                                dp[la][lb + 1] += 1 + min(0, dp[la][lb + 1])
                        else:
                            dp[la][lb + 1] = idx
                            if dp[la][lb + 1] != -1:
                                dp[la][lb + 1] += 1 + min(0, dp[la][lb + 1])

                if dp[len(a)][len(b)] != -1:
                    ans = "YES"
                    break
        if ans == "YES":
            break
    return ans


def main(n: int):
    """
    n 为测试规模，这里将其理解为：
    - 测试用例数量 = n
    - 每个 s、t 的长度在 [1, n] 区间内随机生成
    - 字符集为小写字母
    """
    random.seed(0)
    for _ in range(n):
        len_s = random.randint(1, n)
        len_t = random.randint(1, n)
        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_s))
        t = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_t))
        print(s)
        print(t)
        print(solve_case(s, t))


if __name__ == "__main__":
    # 示例：生成规模为 5 的随机测试
    main(5)