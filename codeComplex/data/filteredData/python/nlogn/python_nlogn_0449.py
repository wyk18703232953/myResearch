import random

def main(n: int):
    # 生成测试数据
    # 1. 随机生成数组 s，长度为 n
    # 2. 随机选择一个位置作为 m 的位置，保证数组中一定包含 m
    if n <= 0:
        return

    # 生成随机数组元素范围可自行调整
    s = [random.randint(1, 10) for _ in range(n)]
    ind_m = random.randint(0, n - 1)
    m = s[ind_m]

    # 下面是原逻辑的无 input() 版本
    try:
        ind = s.index(m)
    except ValueError:
        print(0)
        return

    dp = [0 for _ in range(n)]

    for i in range(ind + 1, n):
        if s[i] < m:
            dp[i] = dp[i - 1] - 1
        elif s[i] > m:
            dp[i] = dp[i - 1] + 1

    for i in range(ind - 1, -1, -1):
        if s[i] < m:
            dp[i] = dp[i + 1] - 1
        elif s[i] > m:
            dp[i] = dp[i + 1] + 1

    d = dict()
    for i in range(ind + 1, n):
        if dp[i] in d:
            d[dp[i]] += 1
        else:
            d[dp[i]] = 1

    ans = 0
    for i in range(ind + 1):
        x = -dp[i]
        if x in d:
            ans += d[x]
        if x + 1 in d:
            ans += d[x + 1]
        if dp[i] == 0 or dp[i] == 1:
            ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)