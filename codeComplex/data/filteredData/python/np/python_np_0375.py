import random
import string

def solve(a, m):
    n = len(a)
    dp = [10 ** 10] * (1 << 20)
    cnt = [0] * (1 << 20)

    def get(x):
        return 1 << (ord(x) - ord('a'))

    for i, v in enumerate(a):
        if i:
            cnt[get(a[i]) | get(a[i - 1])] += 1

    for i in range(m):
        for j in range(1 << m):
            if (1 << i) & j:
                cnt[j] += cnt[j ^ (1 << i)]

    dp[0] = 0

    for i in range(1 << m):
        for j in range(m):
            if not i & (1 << j):
                s = i | (1 << j)
                dp[s] = min(
                    dp[s],
                    dp[i] + n - 1 - cnt[s] - cnt[(1 << m) - 1 - s]
                )
    return dp[(1 << m) - 1]


def main(n):
    # 设定字母种类 m，需满足 1 <= m <= 20
    # 这里选择一个与 n 相关、但不超过 20 的 m
    m = min(20, max(1, n // 5))

    # 生成长度为 n 的随机字符串，仅使用前 m 个小写字母
    alphabet = string.ascii_lowercase[:m]
    a = [random.choice(alphabet) for _ in range(n)]

    ans = solve(a, m)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)