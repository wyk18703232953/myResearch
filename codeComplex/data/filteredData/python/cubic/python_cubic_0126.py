import random
import string

def solve_case(s: str, t: str) -> str:
    if len(t) == 1:
        return "YES" if t in s else "NO"

    n = len(s)
    nxt = [[-1] * 26 for _ in range(n + 1)]
    nxt[-2][ord(s[-1]) - ord('a')] = n - 1
    for i in range(n - 2, -1, -1):
        for c in range(26):
            nxt[i][c] = nxt[i + 1][c]
        nxt[i][ord(s[i]) - ord('a')] = i

    ans = "NO"
    for p in range(len(t)):
        a = t[:p]
        b = t[p:]
        la_len = len(a)
        lb_len = len(b)
        dp = [[-1] * (lb_len + 1) for _ in range(la_len + 1)]
        dp[0][0] = 0
        for la in range(la_len + 1):
            for lb in range(lb_len + 1):
                if dp[la][lb] != -1:
                    if la < la_len:
                        pos = nxt[dp[la][lb]][ord(a[la]) - ord('a')]
                        if pos != -1:
                            if dp[la + 1][lb] != -1:
                                if pos < dp[la + 1][lb] - 1:
                                    dp[la + 1][lb] = pos
                                    dp[la + 1][lb] += 1 + min(0, dp[la + 1][lb])
                            else:
                                dp[la + 1][lb] = pos
                                dp[la + 1][lb] += 1 + min(0, dp[la + 1][lb])
                    if lb < lb_len:
                        pos = nxt[dp[la][lb]][ord(b[lb]) - ord('a')]
                        if pos != -1:
                            if dp[la][lb + 1] != -1:
                                if pos < dp[la][lb + 1] - 1:
                                    dp[la][lb + 1] = pos
                                    dp[la][lb + 1] += 1 + min(0, dp[la][lb + 1])
                            else:
                                dp[la][lb + 1] = pos
                                dp[la][lb + 1] += 1 + min(0, dp[la][lb + 1])
            if dp[la_len][lb_len] != -1:
                ans = "YES"
                break

    return ans


def main(n: int):
    # 生成 n 组测试数据
    random.seed(0)
    tests = n

    for _ in range(tests):
        # 根据规模 n 生成字符串长度（可按需调整策略）
        len_s = random.randint(1, max(1, n))
        len_t = random.randint(1, max(1, n))

        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_s))
        t = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_t))

        print(s)
        print(t)
        print(solve_case(s, t))


if __name__ == "__main__":
    # 示例：调用 main(5) 生成 5 组测试
    main(5)