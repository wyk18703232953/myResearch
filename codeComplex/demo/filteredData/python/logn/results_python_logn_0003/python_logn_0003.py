def main(n):
    # 解释输入结构：
    # 原程序读取两个整数 l, r
    # 在这里将 n 映射为一个规模参数，用来构造确定性的 l 和 r
    # 设定：
    # l = n
    # r = 2*n + 3
    l = n
    r = 2 * n + 3

    x = l ^ r
    a = 2
    if l == r:
        result = 0

    else:
        while a <= x:
            a = a * 2
        result = a - 1

    return result


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的大小进行复杂度实验
    n = 10
    # print(main(n))
    pass