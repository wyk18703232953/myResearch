def getsum(a, b):
    if a % 2 == 0:
        return (a + b) * ((b - a) // 2 + 1) // 2

    else:
        return -(a + b) * ((b - a) // 2 + 1) // 2


def main(n):
    # 生成规模为 n 的测试数据：q 组 [l, r]
    # 这里简单生成 q = n，区间为 [i, i + n]（也可按需要修改生成逻辑）
    q = n
    queries = []
    for i in range(1, q + 1):
        l = i
        r = i + n
        queries.append((l, r))

    # 处理并打印结果
    for l, r in queries:
        if l == r:
            # print(l if l % 2 == 0 else -l)
            pass

        else:
            print(
                getsum(l if l % 2 == 1 else l + 1,
                       r if r % 2 == 1 else r - 1)
                +
                getsum(l if l % 2 == 0 else l + 1,
                       r if r % 2 == 0 else r - 1)
            )


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)