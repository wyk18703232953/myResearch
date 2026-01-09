def main(n):
    # n 表示序列长度
    if n <= 0:
        return

    number_sequence = [i % 10 + 1 for i in range(1, n + 1)]
    number_total = sum(number_sequence)

    current_total = 0
    current_position = 0

    for number in number_sequence:
        current_total = current_total + number
        current_position = current_position + 1
        if current_total >= number_total / 2:
            # print(current_position)
            pass
            break


if __name__ == "__main__":
    main(10)