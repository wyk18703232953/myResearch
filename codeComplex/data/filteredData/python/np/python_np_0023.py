import random

def main(n: int):
    # 生成测试数据：n 和 lis
    # 原程序中 lis 中的值在 0..(1<<22)-1 范围内
    MAX_BITS = 22
    MAX_VAL = (1 << MAX_BITS) - 1

    # 为了保证算法有意义，生成 n 个 [0, 2^22-1] 内的随机数
    random.seed(0)
    lis = [random.randint(0, MAX_VAL) for _ in range(n)]

    # 以下是原逻辑的等价实现
    dp = [-1] * (1 << MAX_BITS)

    # 先将 dp[lis[i]] = lis[i]，并把 lis[i] 依次异或掉每一位（原代码中的处理）
    # 注意：原代码中这样会破坏 lis 的原值，这里为了严格一致也照做
    for i in range(n):
        dp[lis[i]] = lis[i]
        for j in range(MAX_BITS):
            lis[i] ^= (1 << j)

    # SOS DP：对所有 mask 进行转移
    for mask in range(1 << MAX_BITS):
        for i in range(MAX_BITS):
            if (mask & (1 << i)) and dp[mask ^ (1 << i)] != -1:
                dp[mask] = dp[mask ^ (1 << i)]

    # 输出结果，对应原程序对处理后的 lis 中每个 num 输出 dp[num]
    # 这里直接打印到标准输出
    res = []
    for num in lis:
        res.append(str(dp[num]))
    print(" ".join(res))


if __name__ == "__main__":
    # 示例：调用 main，n 可根据需要修改
    main(5)