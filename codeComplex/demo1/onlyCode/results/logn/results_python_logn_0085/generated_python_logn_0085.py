def main(n: int):
    """
    将原先从 input() 读取的区间 [l, r] 改为根据规模 n 生成测试数据。
    这里约定：
      l = n
      r = 2 * n
    你可以根据需要修改生成规则。
    """
    l = n
    r = 2 * n

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
    # 示例：使用 n = 10 运行
    main(10)