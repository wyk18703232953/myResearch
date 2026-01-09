def check(s, t1, t2):
    s1 = len(t1)
    s2 = len(t2)
    n = len(s)
    dp = [[-1] * (s1 + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(s1 + 1):
            if dp[i][j] >= 0:
                if j < s1 and t1[j] == s[i]:
                    if dp[i + 1][j + 1] < dp[i][j]:
                        dp[i + 1][j + 1] = dp[i][j]
                if dp[i][j] < s2 and t2[dp[i][j]] == s[i]:
                    if dp[i + 1][j] < dp[i][j] + 1:
                        dp[i + 1][j] = dp[i][j] + 1
            if dp[i + 1][j] < dp[i][j]:
                dp[i + 1][j] = dp[i][j]
    return dp[n][s1] == s2


def solve_single_case(s, t):
    le = len(t)
    for i in range(le):
        t1 = t[:i]
        t2 = t[i:]
        if check(s, t1, t2):
            return "YES"
    return "NO"


def generate_case(k):
    # Deterministically generate s, t from k
    # Map k to lengths; ensure at least length 1 for t
    len_s = max(1, k)
    len_t = max(1, (k // 2) + 1)

    # Simple deterministic alphabet
    alphabet = "abc"

    # Build s and t deterministically using modular arithmetic
    s_chars = [alphabet[(i * 2 + 1) % len(alphabet)] for i in range(len_s)]
    t_chars = [alphabet[(i * 3 + 2) % len(alphabet)] for i in range(len_t)]

    s = "".join(s_chars)
    t = "".join(t_chars)
    return s, t


def main(n):
    # Interpret n as number of test cases
    if n <= 0:
        return

    for k in range(1, n + 1):
        s, t = generate_case(k)
        ans = solve_single_case(s, t)
        # print(ans)
        pass
if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(5)