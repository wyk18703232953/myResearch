MOD = 998244353

def power(x, n):
    ans = 1
    x %= MOD
    while n:
        if n & 1:
            ans = ans * x % MOD
        x = x * x % MOD
        n //= 2
    return ans

def main(n):
    """
    生成规模为 n 的测试数据并执行原逻辑。
    测试数据策略：构造一个长度为 n 的数组 a，部分位置为 -1，部分为 1..n 的排列前缀。
    """
    # 简单的可重复测试数据构造：
    # 前 half 个位置放实际值（循环取 1..n），后半部分放 -1
    a = [0] * n
    half = n // 2
    for i in range(n):
        if i < half:
            a[i] = (i % n) + 1

        else:
            a[i] = -1

    b = [0] * (n + 1)

    def add(x, v):
        while x <= n:
            b[x] += v
            x += x & -x

    def get(x):
        s = 0
        while x:
            s += b[x]
            x -= x & -x
        return s

    # 已知位置之间的逆序对
    anss = 0
    for i in range(n):
        if a[i] != -1:
            add(a[i], 1)
            anss += get(n) - get(a[i])
    anss %= MOD

    total = 0
    sur = [0] + [1] * n
    for i in range(n):
        if a[i] == -1:
            total += 1

        else:
            sur[a[i]] = 0

    if total == 0:
        # print(anss % MOD)
        pass
        return

    for i in range(1, n + 1):
        sur[i] += sur[i - 1]

    dead = 0
    ansa = 0
    for i in range(n):
        if a[i] != -1:
            ansa += sur[a[i]] * (total - dead) + (sur[n] - sur[a[i]]) * dead

        else:
            dead += 1

    ans = (ansa * 4 + anss * 4 * total + total * total * (total - 1)) % MOD
    ans = ans * power(4 * total, MOD - 2) % MOD
    # print(ans)
    pass

# 示例调用
if __name__ == "__main__":
    main(10)