def get_answer(arr):
    current_sum = 0
    total = sum(arr)
    for index, val in enumerate(arr):
        current_sum += val
        if current_sum >= total / 2:
            return index + 1


def main(n):
    if n <= 0:
        return None
    # 生成一个长度为 n 的整数列表，元素为 1 到 n
    values = [i + 1 for i in range(n)]
    result = get_answer(values)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例调用：使用 n = 10 作为规模
    main(10)