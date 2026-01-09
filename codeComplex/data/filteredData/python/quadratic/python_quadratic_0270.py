def main(n):
    # 映射规则：
    # n 为输入规模，同时作为列表长度和取值上界的基础
    # 定义 m = n，同一规模下两个列表长度相同
    m = n

    # 生成 list1：长度为 n，元素为 1..n
    list1 = [i + 1 for i in range(n)]

    # 生成 list2：长度为 m，元素为 (2*i + 1) % (n + 1)，再处理为非零整数
    # 这样生成的数据既确定，又能形成部分交集
    raw_list2 = [(2 * i + 1) % (n + 1) for i in range(m)]
    list2 = [x if x != 0 else 1 for x in raw_list2]

    # 原算法逻辑：输出 list1 中出现在 list2 中的元素
    s2 = set(list2)
    result = []
    for i in list1:
        if i in s2:
            result.append(str(i))

    if result:
        # print(" ".join(result))
        pass

    else:
        # print()
        pass
if __name__ == "__main__":
    main(10)