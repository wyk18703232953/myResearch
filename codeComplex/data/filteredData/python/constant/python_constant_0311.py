def main(n):
    import random

    # 生成规模为 n 的测试数据，但算法本身固定使用 14 个坑位
    # 这里使用 n 仅作为随机数种子或数据规模的控制参数
    random.seed(n)

    # 原题逻辑固定为 14 个元素，这里根据 n 生成一组长度为 14 的数组 b
    # 例如：元素大小与 n 相关，范围 [0, 2*n]
    global b
    b = [random.randint(0, 2 * max(1, n)) for _ in range(14)]

    def fn(p):
        turns = b[p] // 14
        a = b.copy()
        sm = 0
        a[p] = 0
        for i in range(1, 15):
            a[(p + i) % 14] += turns
        rem = b[p] % 14
        for i in range(p + 1, p + rem + 1):
            a[i % 14] += 1
        for i in range(14):
            if a[i] & 1 == 0:
                sm += a[i]
        return sm

    ans = 0
    for i in range(14):
        if b[i] != 0:
            ans = max(ans, fn(i))

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)