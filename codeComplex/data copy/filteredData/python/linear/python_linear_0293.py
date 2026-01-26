def main(n):
    # 生成长度为 n 的整数列表 a，元素为 i % (n // 2 + 1)，保证确定性
    if n <= 0:
        a = []

    else:
        mod_base = n // 2 + 1
        a = [i % mod_base for i in range(n)]

    d = set(a)
    if 0 in a:
        result = len(d) - 1

    else:
        result = len(d)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以做规模化实验
    main(10)