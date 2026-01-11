def main(n):
    # 生成确定性输入：列表长度为 n
    # 使用简单算术构造：元素为 i % (n // 2 + 1) 形成重复元素
    if n <= 0:
        return  # 无意义规模，直接返回

    lst = [i % (n // 2 + 1) for i in range(n)]

    # 原始逻辑开始
    lst = set(lst)
    lst = list(lst)
    lst.remove(min(lst))
    if len(lst) == 0:
        # print("NO")
        pass

    else:
        # print(min(lst))
        pass
if __name__ == "__main__":
    main(10)