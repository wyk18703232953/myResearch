import random
import string

def check(s: str, t: str) -> bool:
    N = len(t)
    for i in range(1, N + 1):
        # split t into t1:[0,i), t2:[i,N)
        dp = [0] + [-1] * i
        for c in s:
            for j in range(i, -1, -1):
                tmp = dp[j]
                # use c for t2
                if dp[j] != -1 and i + dp[j] < N and t[i + dp[j]] == c:
                    tmp = dp[j] + 1
                # use c for t1
                if j != 0 and t[j - 1] == c:
                    tmp = max(tmp, dp[j - 1])
                dp[j] = tmp
        if dp[i] == N - i:
            return True
    return False


def main(n: int):
    """
    n: problem size parameter, used to control lengths of s and t.
       Here we generate:
         - length of t:  between max(1, n//3) and max(1, n//2)
         - length of s:  between len(t) and max(len(t), n)
    """
    random.seed(0)

    T = 5  # number of test cases to generate
    for _ in range(T):
        # generate t
        len_t = max(1, random.randint(max(1, n // 3), max(1, n // 2)))
        t = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_t))

        # generate s so that len(s) >= len(t) and up to n
        max_s_len = max(len_t, n)
        len_s = random.randint(len_t, max_s_len)
        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_s))

        # run the original logic
        if check(s, t):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    # example: n = 20
    main(20)