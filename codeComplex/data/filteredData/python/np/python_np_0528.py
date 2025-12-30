import random
import string

def solve(N, K, S):
    # 将字符串转为数组：字母 -> 0~25, '?' -> -1
    S = [-1 if ch == '?' else ord(ch) - ord('a') for ch in S]

    def check(x):
        # p[k][i] 表示从位置 i 开始，能放长度为 x 的连续字母 k 的最右端位置
        p = [[N for _ in range(N + 1)] for _ in range(K)]

        for k in range(K):
            keep = 0
            for i in range(N - 1, -1, -1):
                keep += 1
                if S[i] != -1 and S[i] != k:
                    keep = 0
                p[k][i] = p[k][i + 1]
                if keep >= x:
                    p[k][i] = i + x - 1

        # d[s]：集合 s（位掩码）对应的方案的最右端位置
        d = [N] * (1 << K)
        d[0] = -1
        for s in range(1, 1 << K):
            for k in range(K):
                if (s & (1 << k)) and d[s ^ (1 << k)] < N:
                    d[s] = min(d[s], p[k][d[s ^ (1 << k)] + 1])
        return d[(1 << K) - 1] < N

    l, r = 0, N // K
    while l < r:
        mid = (l + r + 1) // 2
        if check(mid):
            l = mid
        else:
            r = mid - 1
    return l


def generate_test_data(n):
    # 简单规则：K 不超过 6，且 K <= n
    K = min(6, max(1, n // 2))
    N = n

    # 随机生成由前 K 个字母和 '?' 组成的字符串
    alphabet = string.ascii_lowercase[:K]
    choices = alphabet + "?"
    S = "".join(random.choice(choices) for _ in range(N))

    return N, K, S


def main(n):
    N, K, S = generate_test_data(n)
    ans = solve(N, K, S)
    print(ans)