import random
import string


def solve_case(s: str, t: str) -> str:
    N = len(t)
    for i in range(1, N + 1):
        dp = [0] + [-1] * i
        for c in s:
            for j in range(i, -1, -1):
                tmp = dp[j]
                if dp[j] != -1 and i + dp[j] < N and t[i + dp[j]] == c:
                    tmp = dp[j] + 1
                if j != 0 and t[j - 1] == c:
                    tmp = max(tmp, dp[j - 1])
                dp[j] = tmp
        if dp[i] == N - i:
            return "YES"
    return "NO"


def main(n: int):
    """
    n 为规模参数，用来生成测试数据。
    这里约定：
      - 生成 T = n 个测试用例
      - 每个用例字符串 s, t 的长度在 [1, n] 之间随机
    """
    random.seed(0)
    T = n
    alphabet = string.ascii_lowercase

    for _ in range(T):
        len_s = random.randint(1, max(1, n))
        len_t = random.randint(1, max(1, n))
        s = ''.join(random.choice(alphabet) for _ in range(len_s))
        t = ''.join(random.choice(alphabet) for _ in range(len_t))
        print(s)
        print(t)
        print(solve_case(s, t))


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)