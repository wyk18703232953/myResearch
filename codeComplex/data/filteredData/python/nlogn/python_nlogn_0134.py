def main(n):
    # 映射含义：
    # n -> 列表长度
    # m, k 由 n 确定性生成
    if n <= 0:
        return

    # 生成参数 m, k
    m = n * 5
    k = n // 2

    # 生成长度为 n 的列表 x，元素确定性构造
    x = [(i * 3) % (n + 7) + 1 for i in range(1, n + 1)]

    # 原算法逻辑
    x.sort(reverse=True)
    if k >= m:
        print(0)
    else:
        for i in range(n):
            k -= 1
            k += x[i]
            if k >= m:
                break
        if k >= m:
            print(i + 1)
        else:
            print(-1)


if __name__ == "__main__":
    main(10)