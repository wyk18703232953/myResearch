def main(n):
    # n 表示列表长度
    if n <= 0:
        return

    # 确定性生成 n 个整数
    # 构造规则：a[i] = i % 5，用于保证奇偶分布相对稳定
    li = [i % 5 for i in range(1, n + 1)]

    lis = [x % 2 for x in li]
    if lis.count(0) > lis.count(1):
        # print(lis.index(1) + 1)
        pass

    else:
        # print(lis.index(0) + 1)
        pass
if __name__ == "__main__":
    main(10)