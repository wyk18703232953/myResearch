def main(n: int):
    """
    将原程序参数化：
    - 不再使用 input()
    - 根据规模 n 生成测试数据 l, r
    这里用一种简单可控的方式生成区间：
        l = n
        r = 2 * n + 3  （保证 r > l 且区间长度随 n 增大）
    """

    l = n
    r = 2 * n + 3

    if l == r:
        print(0)
        return

    x = 1
    while x <= r:
        x = x << 1
    x = x >> 1

    k = x
    while x <= l or x > r:
        if x <= l:
            x += k
        else:
            x -= k
        k = k >> 1

    print(x ^ (x - 1))


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 进行测试
    main(10)