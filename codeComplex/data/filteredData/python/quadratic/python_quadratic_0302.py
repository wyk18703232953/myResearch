def main(n):
    # 生成确定性输入数据：长度为 n 的列表 t
    # 这里构造一种包含重复元素的模式，以匹配原算法行为需求
    # t 的结构为：[i % max(1, n//3) for i in range(n)]
    if n <= 0:
        # print(0)
        pass
        return

    base = max(1, n // 3)
    t = [i % base for i in range(n)]

    sw = 0

    while t != [] and len(t) > 1:
        # 若后缀中找不到与 t[0] 相同的元素，会抛出错误
        # 为保持原逻辑，这里保证构造的数据总能在后面找到相同元素
        # 但若意外构造失败，则跳出循环
        try:
            pr = 1 + t[1:].index(t[0])
        except ValueError:
            break
        sw += pr - 1
        t = t[1:pr] + t[pr+1:]

    # print(sw)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小进行实验
    main(10)