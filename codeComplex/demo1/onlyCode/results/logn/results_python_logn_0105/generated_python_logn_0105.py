def main(n):
    # 根据 n 生成测试数据：构造一对 (l, r)，满足 1 <= l <= r <= n
    # 这里简单生成：l = n // 2, r = n
    if n < 1:
        return
    l = max(1, n // 2)
    r = n

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
    # 示例运行：规模为 10
    main(10)