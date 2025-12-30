import random

def main(n: int):
    # 生成测试数据：n, m, k 和数组 a
    # 这里选择：
    #   m 在 [1, n] 内随机
    #   k 在 [0, max(1, max(a))] 内随机（后面生成 a 后再调整）
    if n <= 0:
        return 0

    # 先生成 a
    # 测试数据策略：元素在 [-10, 10] 范围内随机
    a = [random.randint(-10, 10) for _ in range(n)]

    # m 至少为 1，至多为 n
    m = random.randint(1, n)

    # k 与数据量级相关，这里取 0~10 的随机值
    k = random.randint(0, 10)

    best = 0
    dp = [0] * (n + 1)

    # 预处理前缀和，加速 sum 计算
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]

    for i in range(n):
        b2 = 0
        # 原代码：sum(a[j + 1:i + 1])，用前缀和表示为 prefix[i+1] - prefix[j+1]
        for j in range(max(-1, i - m), i + 1):
            # j == -1 时，对应 sum(a[0:i+1])，此时 prefix 索引要特殊处理
            if j == -1:
                seg_sum = prefix[i + 1] - prefix[0]
                b2 = max(b2, dp[0] - k + seg_sum)
            else:
                seg_sum = prefix[i + 1] - prefix[j + 1]
                b2 = max(b2, dp[j] - k + seg_sum)
        dp[i] = max(b2, a[i] - k)
        best = max(best, dp[i])

    print(best)
    return best

if __name__ == "__main__":
    # 示例：规模 n=10
    main(10)