import random
import math

mod = 1000000007
f = []  # factorial cache


def fact(n, m):
    """Precompute factorials modulo m up to n."""
    global f
    f = [1] * (n + 1)
    for i in range(1, n + 1):
        f[i] = (f[i - 1] * i) % m


def fast_mod_exp(a, b, m):
    res = 1
    a %= m
    while b > 0:
        if b & 1:
            res = (res * a) % m
        a = (a * a) % m
        b >>= 1
    return res


def inverseMod(n, m):
    # m is prime in this problem, use Fermat's little theorem
    return fast_mod_exp(n, m - 2, m)


def ncr(n, r, m):
    if n < 0 or r < 0 or r > n:
        return 0
    if r == 0:
        return 1
    return ((f[n] * inverseMod(f[n - r], m)) % m * inverseMod(f[r], m)) % m


def getCount(n):
    """Count set bits in n."""
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n >>= 1
    return count


def solve_C(s, k):
    """Core logic of original C() using given binary string s and integer k."""
    if k == 0:
        return 1

    # dp[x] = number of times we need to apply popcount to x to get 1
    limit = 1010
    dp = [0] * limit
    for i in range(limit):
        if i == 0 or i == 1:
            continue
        dp[i] = dp[getCount(i)] + 1

    fact(limit, mod)

    ans = 0
    count = 0
    n_len = len(s)

    # Count numbers < s with required property
    for i in range(n_len):
        if s[i] == '0':
            continue
        for j in range(max(count, 1), limit):
            if dp[j] == k - 1:
                ans = (ans + ncr(n_len - i - 1, j - count, mod)) % mod
                if i == 0 and k == 1:
                    ans = (ans + mod - 1) % mod
        count += 1

    # Count s itself if it satisfies property
    count = s.count('1')
    if dp[count] == k - 1:
        ans = (ans + 1) % mod

    return ans


def generate_test_data(n):
    """
    根据规模 n 生成测试数据：
    - 生成一个长度为 L 的二进制串 s，L 在 [1, n] 范围内。
    - 生成一个整数 k，1 <= k <= min(20, L)。
    """
    if n <= 0:
        n = 1
    L = random.randint(1, n)
    # 保证首位为 '1'，避免前导零
    if L == 1:
        s = '1'
    else:
        s = '1' + ''.join(random.choice('01') for _ in range(L - 1))
    k = random.randint(1, min(20, L))
    return s, k


def main(n):
    """
    n 为规模参数，用于生成测试数据，然后调用原逻辑。
    返回值为原程序 C() 的输出结果。
    """
    s, k = generate_test_data(n)
    return solve_C(s, k)


if __name__ == "__main__":
    # 示例：使用规模 10 运行一次
    result = main(10)
    print(result)