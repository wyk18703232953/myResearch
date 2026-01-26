def main(n):
    # 原程序输入结构：一行两个整数 l1, l2
    # 将 n 映射为 (l1, l2)，保证确定性和可规模化
    # 例如：l1 = n，l2 = 2*n + 1
    l1 = n
    l2 = 2 * n + 1

    x = l1 ^ l2
    y = 1
    while y <= x:
        y = y * 2

    # print(y - 1)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值做时间复杂度实验
    main(10)