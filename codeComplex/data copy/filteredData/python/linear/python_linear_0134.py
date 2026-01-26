def bit_count(x):
    ans = 0
    while x:
        x &= x - 1
        ans += 1
    return ans

def core(n_str, k):
    x = len(n_str)
    if n_str == '1':
        return int(k == 0)
    if k == 0:
        return 1
    mod = 10 ** 9 + 7
    dp = [0] * (x + 1)
    dp[1] = 1
    for i in range(2, x + 1):
        dp[i] = dp[bit_count(i)] + 1
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
            ans = (ans + dp1[x - 1 - j][se] - (se == 1 and k == 1)) % mod
            se -= 1
            if se < 0:
                break
        if cou == i:
            ans = (ans + 1) % mod
    return ans

def main(n):
    # n controls the input size: length of the binary string n_str
    # n_str is deterministically generated as a repeating "101" pattern
    if n <= 0:
        # print(0)
        pass
        return
    pattern = "101"
    n_str = (pattern * ((n + len(pattern) - 1) // len(pattern)))[:n]
    # k is also deterministically derived from n
    # keep k reasonably small relative to n to exercise the logic
    k = max(0, (n % 10) - 2)
    result = core(n_str, k)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)