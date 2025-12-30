import random

INF = 9999999999


def main(n):
    # 生成测试数据
    # 生成 n 个不同的正整数作为 l（为了产生更丰富的递增关系）
    l = random.sample(range(1, 10 * n + 1), n)
    # 生成对应的随机代价数组 l2
    l2 = [random.randint(1, 100) for _ in range(n)]

    dp_1 = l2.copy()
    dp_2 = [INF] * n
    dp_3 = [INF] * n

    for i in range(1, n):
        for j in range(i):
            if l[i] > l[j]:
                dp_2[i] = min(dp_2[i], dp_1[j] + l2[i])

    for i in range(1, n):
        for j in range(i):
            if l[i] > l[j]:
                dp_3[i] = min(dp_3[i], dp_2[j] + l2[i])

    x = min(dp_3)
    if x == INF:
        print(-1)
    else:
        print(x)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)