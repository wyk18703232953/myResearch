import random
import string

def solve_case(s, t):
    n = len(s)
    find = [[n] * 26 for _ in range(n + 2)]
    for i in range(n - 1, -1, -1):
        find[i][:] = find[i + 1]
        find[i][ord(s[i]) - ord("a")] = i

    def interleaving(a, b):
        dp = [n] * (len(b) + 1)
        for i in range(len(a) + 1):
            for j in range(len(b) + 1):
                if i == j == 0:
                    dp[j] = -1
                    continue
                res = n
                if i > 0:
                    res = min(res, find[dp[j] + 1][ord(a[i - 1]) - ord("a")])
                if j > 0:
                    res = min(res, find[dp[j - 1] + 1][ord(b[j - 1]) - ord("a")])
                dp[j] = res
        return dp[-1] < n

    return any(interleaving(t[:i], t[i:]) for i in range(len(t)))


def main(n):
    # n: problem scale parameter, will be used as max length of s and t and number of test cases
    random.seed(0)
    T = n  # number of test cases
    for _ in range(T):
        len_s = random.randint(1, n)
        len_t = random.randint(1, n)
        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_s))
        t = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_t))
        if solve_case(s, t):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    # Example run with scale n = 5
    main(5)