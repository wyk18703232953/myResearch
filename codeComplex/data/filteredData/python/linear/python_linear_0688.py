def clc(mid, n):
    sm, i, cp = 0, 1, n
    cur = 1
    while cp + 1 > cur:
        sm = sm + i * cur
        i += 1
        cp -= cur
        cur = cur * mid
    return sm + i * cp

def main(n):
    s = n * (n + 1) // 2  # 最大可行 s，保证通过初始判断

    sm = n * (n + 1) // 2
    dp = [0] * 100005
    x = [0] * 100005
    y = [0] * 100005
    x[0] = 1

    if s + 1 < 2 * n:
        return
    if s > sm:
        return

    l = 0
    r = n
    while r - l > 1:
        mid = (r + l) // 2
        if clc(mid, n) > s:
            l = mid

        else:
            r = mid

    i = 2
    while i < n + 1:
        y[i] = i + r
        y[i] -= 2
        y[i] = y[i] // r
        x[i] = x[y[i]] + 1
        if dp[x[i]] == 0:
            dp[x[i]] = i
        i = i + 1

    mx = x[n]
    ip = n
    s = s - clc(r, n)

    while s != 0:
        if x[ip] != x[ip - 1]:
            ip = ip - 1
        if s > mx - x[ip]:
            y[ip] = dp[mx]
            mx = mx + 1
            s -= mx - x[ip]
            x[ip] = mx
            dp[mx] = ip

        else:
            y[ip] = dp[s + x[ip] - 1]
            s = 0
        ip = ip - 1

    i = 2
    while i < n + 1:
        # print(y[i])
        pass
        i = i + 1

if __name__ == "__main__":
    main(10)