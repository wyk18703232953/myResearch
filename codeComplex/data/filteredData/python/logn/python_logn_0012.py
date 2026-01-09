def main(n):
    # 对于时间复杂度实验，将 n 映射为 r 的值，l 固定为 0
    # 原程序输入结构：单行两个整数 l, r
    # 这里构造：l = 0, r = n
    l, r = 0, n

    x = 64
    while x >= 0 and (l & (1 << x)) == (r & (1 << x)):
        x -= 1
    result = (1 << (x + 1)) - 1

    # print(result)
    pass
if __name__ == "__main__":
    main(10)