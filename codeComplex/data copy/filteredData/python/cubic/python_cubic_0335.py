import sys

mod = 998244353

def main(n):
    # n: input size, interpreted as length of array a
    if n <= 0:
        # print(0)
        pass
        return

    # Deterministic generation of a: a sorted list of n integers
    # Example: a[i] = (i * 2 + 1) for i in range(n)
    a = [(i * 2 + 1) for i in range(n)]

    a.sort()
    dp = [1] + [0] * n
    for i in range(1, n + 1):
        x, pt = 1, i - 2
        while pt >= 0 and 2 * a[pt] > a[i - 1]:
            x = x * (n - pt - 2) % mod
            pt -= 1
        dp[i] = (dp[i - 1] * (n - i) + dp[pt + 1] * x) % mod
    # print(dp[-1])
    pass
if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(10)