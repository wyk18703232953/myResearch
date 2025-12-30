import random

def main(n):
    # 生成测试数据
    # a: 随机整数序列，值域 [1, 2*n]
    # cost: 随机正成本，值域 [1, 10^3]
    a = [random.randint(1, 2 * n) for _ in range(n)]
    cost = [random.randint(1, 1000) for _ in range(n)]

    ans = float("inf")
    for i in range(n):
        m, r = float("inf"), float("inf")
        # 左侧找比 a[i] 小的最小 cost
        for j in range(i):
            if a[j] < a[i]:
                m = min(m, cost[j])
        # 右侧找比 a[i] 大的最小 cost
        for k in range(i + 1, n):
            if a[k] > a[i]:
                r = min(r, cost[k])
        ans = min(ans, cost[i] + m + r)

    result = ans if ans != float("inf") else -1
    print(result)
    return result

if __name__ == "__main__":
    # 示例：规模为 5
    main(5)