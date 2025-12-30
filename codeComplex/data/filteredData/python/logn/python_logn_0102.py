def main(n: int):
    # 这里根据规模 n 生成测试数据 (l, r)
    # 示例：生成一个相对有代表性的区间 [l, r]
    # l 在 [0, n] 中，r 在 (l, 2n] 中
    # 为了简单和可重复，这里直接按规则构造，而不用随机
    l = n // 3
    r = n + (n // 2) + 1
    if r < l:
        r = l

    if l == r:
        print(0)
    else:
        if (r & (r - 1) == 0):
            print(r ^ (r - 1))
        else:
            x = l ^ r
            p = 1
            while p <= x:
                p *= 2
            print(p - 1)


if __name__ == "__main__":
    # 示例：调用 main，规模可按需要调整
    main(10)