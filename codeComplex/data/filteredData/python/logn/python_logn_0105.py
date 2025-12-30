def main(n: int):
    # 根据 n 生成测试数据：
    # 将 n 映射到一个合理区间作为 l, r 的上界
    # 这里简单设置：
    #   l 在 [0, n]
    #   r 在 [l, min(2n, l + n)] 之间
    # 为保证 l <= r，构造如下：
    l = n // 3
    r = n // 3 * 2 + (n % 3)

    # 保证 r >= l
    if r < l:
        l, r = r, l

    # 原始逻辑
    if l == r:
        print(0)
    else:
        if (r & (r - 1)) == 0:
            print(r ^ (r - 1))
        else:
            x = l ^ r
            p1 = 1
            while p1 <= x:
                p1 *= 2
            print(p1 - 1)


if __name__ == "__main__":
    # 示例：可自行修改 n 的值进行测试
    main(10)