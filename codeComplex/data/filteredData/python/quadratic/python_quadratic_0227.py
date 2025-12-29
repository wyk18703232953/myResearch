import random

INF = 9999999999


def main(n: int):
    # 生成测试数据
    # 保证 n >= 1
    if n <= 0:
        return

    # 随机生成 l 和 l2
    # l 中元素不一定有序，以测试一般情况
    l = [random.randint(1, n * 2) for _ in range(n)]
    l2 = [random.randint(1, 10) for _ in range(n)]

    dp_1 = l2.copy()
    dp_2 = [INF] * n
    dp_3 = [INF] * n

    for i in range(1, n):
        for j in range(i):
            if l[i] > l[j]:
                dp_2[i] = min(dp_2[i], dp_1[j] + l2[i])

        for j in range(i):
            if l[i] > l[j]:
                dp_3[i] = min(dp_3[i], dp_2[j] + l2[i])

    x = min(dp_3)
    if x == INF:
        print(-1)
    else:
        print(x)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)