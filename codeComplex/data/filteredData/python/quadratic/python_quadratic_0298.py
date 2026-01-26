def main(n):
    # 生成确定性的输入列表：长度为 n，元素为 i % max(1, n // 3)
    if n <= 0:
        # print(0)
        pass
        return
    k = max(1, n // 3)
    lst = [i % k for i in range(n)]

    c = 0
    while len(lst) != 0:
        p = lst[0]
        del lst[0]
        i = lst.index(p)
        c += i
        del lst[i]
    # print(c)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值做实验
    main(10)