import sys

int1 = lambda x: int(x)-1
p2D = lambda x: print(*x, sep="\n")
inf = 10**16
md = 10**9+7

def main(n):
    if n <= 0:
        return

    k = max(1, n // 5)
    s_len = n

    s = []
    for i in range(s_len):
        if i % 7 == 0:
            s.append(-1)
        else:
            s.append((i * 3 + k) % k)

    def ok(m):
        nxt = [[s_len]*(s_len+1) for _ in range(k)]
        for j in range(k):
            cnt = 0
            ni = s_len
            nxtj = nxt[j]
            for i in range(s_len - 1, -1, -1):
                if s[i] == -1 or s[i] == j:
                    cnt += 1
                else:
                    cnt = 0
                if cnt >= m:
                    ni = i
                nxtj[i] = ni
        dp = [s_len+1]*(1 << k)
        dp[0] = 0
        for bit in range(1 << k):
            l = dp[bit]
            if l + m > s_len:
                continue
            for j in range(k):
                if bit >> j & 1:
                    continue
                i = nxt[j][l]
                if i + m <= s_len:
                    nbit = bit | (1 << j)
                    if dp[nbit] > i + m:
                        dp[nbit] = i + m
        return dp[-1] <= s_len

    l, r = 0, s_len // max(1, k) + 1
    while l + 1 < r:
        m = (l + r) // 2
        if ok(m):
            l = m
        else:
            r = m

    print(l)

if __name__ == "__main__":
    main(50)