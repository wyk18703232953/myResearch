import random

def main(n):
    # 生成测试数据
    # 随机生成参数 l, r, x 和难度数组 Cs
    # 为了可控，难度值在 [1, 100] 范围内
    Cs = sorted(random.randint(1, 100) for _ in range(n))
    total_sum = sum(Cs)
    l = random.randint(0, max(0, total_sum - 50))
    r = random.randint(l, total_sum)
    x = random.randint(0, max(0, Cs[-1] - Cs[0]))

    probs = 0
    for i in range(1, 2 ** n):
        currsub = [Cs[j] for j in range(n) if (i & (1 << j))]
        if len(currsub) > 1 and l <= sum(currsub) <= r and currsub[-1] - currsub[0] >= x:
            probs += 1

    print(probs)


if __name__ == "__main__":
    # 示例：运行规模为 n=5
    main(5)