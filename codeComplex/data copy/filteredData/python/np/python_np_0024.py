import sys

maxbits = 22
maxmask = 1 << maxbits

def main(n):
    if n <= 0:
        return

    a = [i % maxmask for i in range(1, n + 1)]

    dp = [-1] * maxmask
    for x in a:
        dp[x] = x

    for exp in range(maxbits):
        bit = 1 << exp
        for i in range(maxmask):
            if i & bit:
                if dp[i] == -1:
                    dp[i] = dp[i - bit]

    maxx = maxmask - 1
    out = []
    for i in range(n):
        out.append(str(dp[maxx ^ a[i]]))
    sys.stdout.write(" ".join(out))


if __name__ == "__main__":
    main(10)