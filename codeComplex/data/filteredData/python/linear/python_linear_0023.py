def main(n):
    # 生成一个长度为 n 的整数列表，元素为 i 的平方
    arr = [i * i for i in range(1, n + 1)]
    # 模拟原程序对输入行取模 2 后的列表 l
    l = [x % 2 for x in arr]
    # print(l.index(sum(l) == 1) + 1)
    pass
if __name__ == "__main__":
    main(10)