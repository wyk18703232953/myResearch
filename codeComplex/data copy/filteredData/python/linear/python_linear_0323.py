def main(n):
    # n 表示初始列表和删除列表的长度
    x = n

    # 确定性生成初始列表 list1
    # 使用字符串形式保证和原程序的类型一致
    list1 = [str(i % 5) for i in range(x)]

    # 确定性生成第二轮输入（要删除的元素）
    delete_values = [str((i + 2) % 5) for i in range(x)]

    # 保持原算法逻辑：顺序删除在 list1 中第一次出现的值
    for value in delete_values:
        if value in list1:
            list1.remove(value)

    # print(len(list1))
    pass
if __name__ == "__main__":
    main(10)