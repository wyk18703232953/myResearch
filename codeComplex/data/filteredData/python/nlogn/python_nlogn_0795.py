import random

def main(n: int):
    # 生成测试数据
    # 生成一个有序数组 l，长度为 n
    # 这里假设元素为 0~10*n 之间的随机递增序列
    l = sorted(random.sample(range(0, 10 * n), n))
    # 生成 k，范围在 1 到 n 之间
    k = random.randint(1, n)

    cost = l[n - 1] - l[0]
    if k == 1:
        result = cost
    else:
        diff = [0 for _ in range(n - 1)]
        for i in range(n - 1):
            diff[i] = l[i + 1] - l[i]
        diff = sorted(diff, reverse=True)
        result = cost - sum(diff[:k - 1])

    # 按原程序行为，只输出结果
    print(result)


if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(10)