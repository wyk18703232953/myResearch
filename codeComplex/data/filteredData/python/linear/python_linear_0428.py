def main(n):
    # n 表示测试用例数量
    test = max(1, n)

    first = []
    for i in range(test):
        # 为第 i 个测试用例生成一个确定性的整数列表
        # 列表长度为 i+1，每个元素为 (i+1)*j，其中 j 从 1 到 i+1
        list_ = [(i + 1) * (j + 1) for j in range(i + 1)]
        sum_ = sum(list_)
        first.append(sum_)

    first_sum = first[0]
    count = 0
    for value in first:
        if first_sum < value:
            count += 1
        else:
            continue
    print(count + 1)


if __name__ == "__main__":
    # 示例调用：可以修改 n 以实验不同规模
    main(5)