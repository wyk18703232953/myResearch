# Converted version with parameterized main(n).
# n: scale parameter used to generate (n_str, k) as test data.

def bit_count(x):
    ans = 0
    while x:
        x &= x - 1
        ans += 1
    return ans

def solve(n_str, k):
    x = len(n_str)
    if n_str == '1':
        return int(k == 0)
    if not k:
        return 1

    mod = 10 ** 9 + 7

    # dp[i] = number of times we have to apply popcount until we reach 1, starting from i
    dp = [0] * (x + 1)
    dp[1] = 1
    for i in range(2, x + 1):
        dp[i] = dp[bit_count(i)] + 1

    # dp1[length][set_bits] = C(length, set_bits) modulo mod
    dp1 = [[0] * (x + 1) for _ in range(x + 1)]
    for i in range(x + 1):
        dp1[i][0] = 1
    for i in range(1, x + 1):
        for j in range(1, i + 1):
            dp1[i][j] = (dp1[i - 1][j - 1] + dp1[i - 1][j]) % mod

    ans = 0
    cou = n_str.count('1')

    for i in range(1, x + 1):
        if dp[i] != k:
            continue
        se = i
        for j in range(x):
            if n_str[j] == '0':
                continue
            # choose remaining 'se' ones from remaining positions
            add_val = dp1[x - 1 - j][se]
            if se == 1 and k == 1:
                add_val -= 1
            ans = (ans + add_val) % mod
            se -= 1
            if se < 0:
                break
        if cou == i:
            ans = (ans + 1) % mod

    return ans

def main(n):
    """
    n: integer scale parameter.
    We generate a test binary string n_str of length n and a k based on n,
    then run the original logic and print the result.

    Test data generation strategy:
      - n_str: '1' + '0'*(n-2) + '1' if n >= 2, else '1'
      - k: min(3, n)  (just an example choice depending on n)
    """
    if n <= 0:
        # trivial case: nothing to do
        print(0)
        return

    if n == 1:
        n_str = '1'
    else:
        # binary string of length n with two ones at ends as a sample
        n_str = '1' + '0' * (n - 2) + '1'

    # choose k depending on n; you can adjust this as needed
    k = min(3, n)

    ans = solve(n_str, k)
    print(ans)

if __name__ == "__main__":
    # Example: call main with some scale, e.g., n = 10
    main(10)