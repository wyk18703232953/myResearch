from sys import stdin


def main():
    n = int(input())
    aa = list(map(int, input().split()))
    dp = [aa]
    for i in range(n - 1, 0, -1):
        aa = aa[:]
        for j in range(i):
            aa[j] ^= aa[j + 1]
        del aa[-1]
        dp.append(aa)
    aa = dp[0]
    for i, bb in enumerate(dp[1:], 1):
        a = aa[0]
        for j, b in enumerate(bb):
            c = aa[j + 1]
            bb[j] = max(a, b, c)
            a = c
        aa = bb
    input()
    res = stdin.read().splitlines()
    for i, s in enumerate(res):
        lo, hi = map(int, s.split())
        res[i] = str(dp[hi - lo][lo - 1])
    print('\n'.join(res))


if __name__ == '__main__':
    main()
