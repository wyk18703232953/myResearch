def main(n):
    # 映射含义：
    # n -> 原程序中的 n（数组长度）
    # m, k 由 n 确定性生成
    # line 由 n 确定性生成

    # 合理设置 m, k 保证可规模化
    m = n * 5 + 3          # 目标值
    k = n // 3 + 1         # 初始值

    # 生成确定性的 line 数组，长度为 n
    # 元素大小随 n 线性增长，保证规模感
    line = [(i * 2 + 1) % (3 * n + 7) + 1 for i in range(n)]

    line.sort(reverse=True)
    count = 0
    if k >= m:
        # print(count)
        pass
        return
    for i in range(n):
        k += line[i] - 1
        count += 1
        if k >= m:
            # print(count)
            pass
            return
    # print(-1)
    pass
if __name__ == "__main__":
    main(10)