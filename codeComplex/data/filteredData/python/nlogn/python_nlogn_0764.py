def main(n):
    # n 表示测试用例数量 t
    t = n

    for case_id in range(t):
        # 为每个用例生成不同规模的数组长度和 n_value
        # 这里将数组长度设置为 case_id + 3，保证长度至少为 3
        length = case_id + 3
        n_value = length + 2  # 保证和数组长度有一定差异，但保持确定性

        # 生成长度为 length 的确定性整数数组
        # 使用简单算术构造：arr[i] = (i * 3 + case_id) % (length + 5) + 1
        arr = [(i * 3 + case_id) % (length + 5) + 1 for i in range(length)]

        arr.sort()
        a = arr[-2]
        result = min(a - 1, n_value - 2)
        print(result)


if __name__ == "__main__":
    main(10)