def sumTillN(n):
    return (n * (n + 1)) // 2


def main(n):
    """
    n: 问题规模（正整数）
    自动生成 k，并按照原算法逻辑计算并返回 midEat。
    这里构造一个必有解的 k：
        任选一个 eat ∈ [0, n]，令 k = sumTillN(n - eat) - eat，
    则原算法在给定 (n, k) 时一定能找到该 eat。
    """
    # 1. 生成测试数据：随机选择一个 eat，使得问题有解
    # 为了可复现，这里不使用随机，直接取 eat = n // 3
    eat_true = n // 3
    k = sumTillN(n - eat_true) - eat_true

    # 2. 原算法逻辑（去掉 input，封装在 main 中）
    minEat = 0
    maxEat = n
    midEat = 0

    while minEat <= maxEat:
        midEat = (minEat + maxEat) // 2
        x = sumTillN(n - midEat)
        if x == k + midEat:
            break
        elif x > k + midEat:
            minEat = midEat + 1
        else:
            maxEat = midEat - 1

    # 输出结果以符合原程序行为
    print(midEat)
    return midEat


# 示例运行
if __name__ == "__main__":
    main(10)