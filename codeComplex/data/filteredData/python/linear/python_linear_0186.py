def main(n):
    # n 表示序列长度
    if n <= 0:
        return

    # 确定性生成测试数据：1, 2, ..., n
    number_sequence = [i for i in range(1, n + 1)]
    number_total = sum(number_sequence)

    current_total = 0
    current_position = 0

    for number in number_sequence:
        current_total += number
        current_position += 1
        if current_total >= number_total / 2:
            # print(current_position)
            pass
            break


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的规模
    main(10)