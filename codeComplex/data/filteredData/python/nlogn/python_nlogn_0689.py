import random

def main(n):
    # 生成测试数据：n, m, l1, l2
    # 可根据需要调整数据生成策略
    m = random.randint(1, max(1, n))           # m ∈ [1, n]
    l1 = [random.randint(1, 100) for _ in range(n)]
    l2 = [random.randint(1, 100) for _ in range(m)]

    # 以下为原逻辑
    l1.sort()
    l2.sort()
    l2 = l2[::-1]

    if n == 1:
        if l1[0] != min(l2):
            print(-1)
        else:
            print(sum(l2))
    elif max(l1) > min(l2):
        print(-1)
    else:
        l1 = l1[::-1]
        if min(l2) == l1[0]:
            print(sum(l2) + (sum(l1) - l1[0]) * m)
        else:
            print(sum(l2) + l1[0] + sum(l1[1:]) * m - l1[1])


if __name__ == "__main__":
    # 示例：调用 main，规模为 5
    main(5)