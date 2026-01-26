def main(n):
    # n 表示序列 a 的长度，同时也用作查询序列 b 的长度
    if n <= 0:
        return

    # 构造确定性序列 a 和查询序列 b
    # a: ["v0", "v1", ..., "v{n-1}"]
    # b: 先依次查询 a 中的元素，再查询若干不存在的元素
    a = ["v{}".format(i) for i in range(n)]
    b = ["v{}".format(i) for i in range(n)] + ["x{}".format(i) for i in range(n)]

    d = {}
    k = 0

    # 原始程序第一段：构建字典
    for i in range(len(a)):
        d[a[i]] = i

    # 原始程序第二段：处理查询
    for s in b:
        if s in d and d[s] != -1:
            c = d[s]
            # print(c - k + 1, end=' ')
            pass
            for i in range(k, c + 1):
                d[a[i]] = -1
            k = c + 1

        else:
            # print(0, end=' ')
            pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)