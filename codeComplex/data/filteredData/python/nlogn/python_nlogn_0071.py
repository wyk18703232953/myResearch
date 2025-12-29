import random

def main(n):
    # 生成测试数据
    # 随机生成 k，范围 [1, n]
    k = random.randint(1, n)
    
    dp = []
    # 生成 n 组 (p, t) 数据
    # p 和 t 的范围可根据需要调整，这里假设为 [1, 100]
    for _ in range(n):
        p = random.randint(1, 100)
        t = random.randint(1, 100)
        dp.append((p, -t))

    # 原逻辑
    dp.sort(reverse=True)
    result = dp.count(dp[k - 1])
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)