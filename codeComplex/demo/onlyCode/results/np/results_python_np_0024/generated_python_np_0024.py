def main(n):
    import sys
    maxbits = 22
    maxmask = 1 << maxbits
    dp = [-1] * maxmask
    a = [i % maxmask for i in range(1, n + 1)]
    b = a[:]
    P = [0] * n
    for i in a:
        dp[i] = i
    for exp in range(maxbits):
        for i in range(maxmask):
            if i & (1 << exp):
                if dp[i] == -1:
                    dp[i] = dp[i - (1 << exp)]
    res = []
    for i in range(n):
        maxx = maxmask - 1
        res.append(dp[maxx ^ a[i]])
    return res

if __name__ == "__main__":
    out = main(10)
    print(" ".join(str(x) for x in out))