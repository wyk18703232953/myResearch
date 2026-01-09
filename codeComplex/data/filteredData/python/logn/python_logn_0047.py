def main(n):
    # 解释输入结构：
    # 原程序读取两个整数 m, n
    # 这里令“规模参数 n”控制 m 和 k 的大小等级和值
    #
    # 构造方式（完全确定性）：
    # m = n
    # k = n // 2
    m = n
    k = n // 2

    res = m ^ k
    s = bin(res)
    s = s[2:]
    s = int(s)
    if s == 0:
        # print(0)
        pass

    else:
        s = str(s)
        res = (2 ** len(s)) - 1
        # print(res)
        pass
if __name__ == "__main__":
    main(10)