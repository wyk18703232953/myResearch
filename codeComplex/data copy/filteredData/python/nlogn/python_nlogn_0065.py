def main(n):
    # n 表示数组长度
    if n <= 0:
        # print(0)
        pass
        return

    # 确定性生成数组：从 1 到 n 的整数
    a = list(range(1, n + 1))

    # 原始逻辑重构为非交互形式
    a = sorted(a)
    s = 0
    c = 0
    total_sum = sum(a)
    while s <= total_sum:
        s += a.pop()
        c += 1
    # print(c)
    pass
if __name__ == "__main__":
    main(10)