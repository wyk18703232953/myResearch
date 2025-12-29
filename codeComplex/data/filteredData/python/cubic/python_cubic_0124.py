import random
import string

def solve_one_case(s: str, t: str) -> str:
    N = len(t)
    for i in range(1, N + 1):
        # dp[l][j]: using first l chars of s, having matched t1[0:j],
        #           how many chars of t2 have been matched (or -1 if impossible)
        dp = [[0] + [-1] * i for _ in range(len(s) + 1)]
        for l, c in enumerate(s):
            for j in range(i + 1):
                dp[l + 1][j] = dp[l][j]
                # use c for t2 (suffix)
                if dp[l][j] != -1:
                    if i + dp[l][j] < N and t[i + dp[l][j]] == c:
                        dp[l + 1][j] = dp[l][j] + 1
                # use c for t1 (prefix)
                if j != 0 and c == t[j - 1]:
                    if dp[l][j - 1] > dp[l + 1][j]:
                        dp[l + 1][j] = dp[l][j - 1]
        if dp[-1][i] == N - i:
            return "YES"
    return "NO"


def main(n: int):
    """
    n: problem scale parameter.
       - We will generate T = n test cases.
       - For each test, s and t are random lowercase strings of length in [1, n].
    """
    random.seed(0)
    T = n
    print(T)
    for _ in range(T):
        len_s = random.randint(1, n)
        len_t = random.randint(1, n)
        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_s))
        t = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_t))
        # Print test data (optional, can be removed if only answers are required)
        print(s)
        print(t)
        ans = solve_one_case(s, t)
        print(ans)


if __name__ == "__main__":
    # example run with n = 5
    main(5)