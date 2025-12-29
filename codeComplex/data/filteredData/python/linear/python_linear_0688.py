def clc(mid, n):
    sm, i, cp = 0, 1, n
    cur = 1
    while cp + 1 > cur:
        sm += i * cur
        i += 1
        cp -= cur
        cur *= mid
    return sm + i * cp

def main(n):
    # 根据 n 生成测试数据，这里简单设定 s 在可行范围内
    # sm 是最大可行 s，保证 s 满足题目原约束
    sm = n * (n + 1) // 2
    # 生成一个中等偏上的 s，且 >= 2n - 1，以通过原有的判断
    s = max(2 * n - 1, sm * 2 // 3)

    dp = [0] * 100005
    x = [0] * 100005
    y = [0] * 100005
    x[0] = 1

    if s + 1 < 2 * n:
        print("No")
        return
    if s > sm:
        print("No")
        return
    else:
        print("Yes")

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
        y[i] //= r
        x[i] = x[y[i]] + 1
        if dp[x[i]] == 0:
            dp[x[i]] = i
        i += 1

    mx = x[n]
    ip = n
    s -= clc(r, n)

    while s != 0:
        if x[ip] != x[ip - 1]:
            ip -= 1
        if s > mx - x[ip]:
            y[ip] = dp[mx]
            mx += 1
            s -= mx - x[ip]
            x[ip] = mx
            dp[mx] = ip
        else:
            y[ip] = dp[s + x[ip] - 1]
            s = 0
        ip -= 1

    i = 2
    while i < n + 1:
        print(y[i])
        i += 1