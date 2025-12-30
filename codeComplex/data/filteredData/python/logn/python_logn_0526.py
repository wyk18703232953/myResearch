def size_of_group(i: int) -> int:
    return 9 * 10 ** (i - 1) * i


def find_group_data(k: int, i: int = 1):
    diff = k - size_of_group(i)
    if diff <= 0:
        return k, i
    return find_group_data(diff, i + 1)


def get_sequence_number(num: int) -> str:
    """Return the num-th digit in the infinite sequence 123456789101112..."""
    k, g = find_group_data(num)
    # index is zero-based within the group
    index_in_group = k - 1
    start_number = 10 ** (g - 1)
    number = start_number + index_in_group // g
    digit_index = index_in_group % g
    return str(number)[digit_index]


def main(n: int):
    """
    生成规模为 n 的测试数据，并输出对应的结果。
    这里的测试数据：取所有从 1 到 n 的位置，依次输出该位置上的数字。
    """
    for i in range(1, n + 1):
        print(get_sequence_number(i))


if __name__ == "__main__":
    # 示例：当 n = 20 时，输出序列前 20 个位置上的数字
    main(20)