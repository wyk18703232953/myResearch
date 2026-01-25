def main(n):
    # 保证 n 为正整数
    if n <= 0:
        n = 1

    # 生成确定性的 x
    # 使用与 n 相关的简单算术构造，确保同一 n 下 x 固定
    x = (n * 7) ^ (n << 1)

    # 生成确定性的集合 a，规模为 n
    # 使用 i, i//2, i%k 等简单算术构造
    a = set((i * 3 + (i // 2) ^ (i % 5)) for i in range(1, n + 1))

    # 原算法逻辑
    if len(a) < n:
        print(0)
    else:
        d = set()
        p = 0
        for i in a:
            v = i & x
            d.add(v)
            if v != i and v in a:
                print(1)
                p = 1
                break
        if len(d) < n and p == 0:
            print(2)
        elif p != 1:
            print(-1)


if __name__ == "__main__":
    # 示例：可根据需要修改 n 来做规模实验
    main(10)