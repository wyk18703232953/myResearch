mod = int(1e9 + 7)
MAXV = 100000

def main(n: int):
    # 1. 根据 n 生成测试数据 a
    # 这里示例：生成长度为 n 的数组，元素在 [1, MAXV] 范围内
    # 为可重复、简单起见，用一个确定性序列
    a = [(i % MAXV) + 1 for i in range(n)]

    # 2. 预处理
    freq = {i: 0 for i in range(MAXV + 1)}
    power = {0: 1}
    for i in range(1, MAXV + 1):
        power[i] = (2 * power[i - 1]) % mod

    # 3. 统计频率
    for v in a:
        if 1 <= v <= MAXV:
            freq[v] += 1

    # 4. DP 计算
    dp = {i: 0 for i in range(MAXV + 1)}
    for gcd in range(MAXV, 0, -1):
        mult = 2
        total = freq[gcd]
        complement = 0
        while mult * gcd <= MAXV:
            total += freq[mult * gcd]
            complement += dp[mult * gcd]
            mult += 1
        dp[gcd] = (power[total] - 1 - complement + mod) % mod

    # 5. 输出结果
    # print(dp[1])
    pass
if __name__ == "__main__":
    # 示例调用：n 可以按需要修改或由外部调用 main(n)
    main(10)