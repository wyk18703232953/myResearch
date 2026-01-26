def main(n):
    # n 表示列表长度
    if n <= 0:
        return

    # 确定性生成长度为 n 的整数列表
    # 构造方式：a[i] = (i * 3 + 1) % 10
    lst = [(i * 3 + 1) % 10 for i in range(n)]

    evens = []
    odds = []

    for e, x in enumerate(lst):
        if x % 2 == 0:
            evens.append(e + 1)

        else:
            odds.append(e + 1)

    if len(evens) < len(odds):
        # print(evens[0] if evens else -1)
        pass

    else:
        # print(odds[0] if odds else -1)
        pass
if __name__ == "__main__":
    # 示例：使用 n=10 作为输入规模
    main(10)