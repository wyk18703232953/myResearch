maxnum = 1005
mod = 1000000007

# Precompute dp, f, c once since maxnum is fixed
dp = [[0] * maxnum for _ in range(maxnum)]
f = [0] * maxnum
c = [[0] * maxnum for _ in range(maxnum)]

def cntone(num):
    tmps = bin(num)[2:]
    cnt = 0
    for ch in tmps:
        if ch == '1':
            cnt += 1
    return cnt

def precompute():
    # precompute f
    for i in range(1, maxnum):
        if i == 1:
            f[i] = 0

        else:
            f[i] = f[cntone(i)] + 1

    # precompute binomial coefficients c
    for i in range(maxnum):
        if i == 0:
            c[i][0] = 1
            continue
        for j in range(i + 1):
            if j == 0:
                c[i][j] = 1

            else:
                c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % mod

def solve_for(s0, k):
    s1 = s0[::-1]
    lens1 = len(s1)

    # reset relevant part of dp for current length
    for i in range(lens1):
        for j in range(lens1 + 1):
            dp[i][j] = 0

    for i in range(lens1):
        if i == 0:
            dp[i][0] = 1
            if s1[i] == '1':
                dp[i][1] = 1

            else:
                dp[i][1] = 0
            continue

        else:
            for j in range(0, i + 2):
                if j == 0:
                    dp[i][j] = 1
                    continue
                if s1[i] == '1':
                    dp[i][j] = (dp[i - 1][j - 1] + c[i][j]) % mod

                else:
                    dp[i][j] = dp[i - 1][j] % mod

    ans = 0

    for i in range(1, lens1 + 1):
        if f[i] == k - 1:
            ans = (ans + dp[lens1 - 1][i]) % mod

    if k == 0:
        ans = 1
    elif k == 1:
        ans -= 1

    else:
        ans = ans
    return ans

def main(n):
    if n < 1:
        n = 1
    if n >= maxnum:
        n = maxnum - 1

    precompute()

    # Deterministically generate s0 and k from n
    # s0: binary string of length n, pattern repeats "101"
    pattern = "101"
    s0_chars = []
    for i in range(n):
        s0_chars.append(pattern[i % len(pattern)])
    s0 = "".join(s0_chars)

    # k cycles through a small range based on n
    k = (n % 10) + 1

    result = solve_for(s0, k)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)