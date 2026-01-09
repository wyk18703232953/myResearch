def main(n):
    # 生成与原程序输入结构一致的测试数据："x y"
    # 将 n 作为第一个整数，第二个整数为 2*n（可随 n 线性扩展）
    x = n
    y = 2 * n

    lst = [x, y]

    if lst[1] > 2 * lst[0] - 1:
        # print(0)
        pass

    else:
        countr = 0
        if lst[1] % 2 == 1:
            countr = (lst[1] - 1) // 2

        else:
            countr = (lst[1] - 2) // 2
        if lst[1] > lst[0] + 1:
            countr = countr - lst[1] + lst[0] + 1
        # print(countr)
        pass
if __name__ == "__main__":
    main(10)