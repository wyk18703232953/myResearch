import random

def main(n):
    # 1. 生成测试数据
    # n: 过滤器数量
    # 为了构造完整输入，还需要生成 m, k
    #
    # 约束依据原题（可自行调整范围）：
    # 1 ≤ n ≤ 200000
    # 1 ≤ m, k ≤ 10^9
    #
    # 这里简单设置：
    # m 在 [1, n * 2] 范围内
    # k 在 [1, m * 2] 范围内
    # filters[i] 在 [1, 10^9] 范围内

    if n <= 0:
        return

    m = random.randint(1, max(1, n * 2))
    k = random.randint(1, max(1, m * 2))
    filters = [random.randint(1, 10**9) for _ in range(n)]

    # 2. 原逻辑实现
    filters.sort()

    supply_filters_needed = 0
    if k < m:
        spots = k
        end = n - 1
        while spots < m and end >= 0:
            spots += filters[end] - 1
            supply_filters_needed += 1
            end -= 1

        if spots < m:
            print(-1)
        else:
            print(supply_filters_needed)
    else:
        print(0)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可根据需要调整
    main(10)