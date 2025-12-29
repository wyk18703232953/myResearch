def main(n: int):
    results = []

    for digit in range(1, n + 1):
        if digit <= 9:
            results.append(str(digit))
            continue

        start_range = 1
        end_range = 9
        power = 1
        digit_count = 2

        # 找到 digit 所在的区间
        while not (start_range <= digit <= end_range):
            start_range = end_range + 1
            end_range = 9 * 10 ** power * digit_count + start_range - 1
            power += 1
            digit_count += 1

        # 计算 offset_number 和所在的具体数字
        offset_number = (digit - start_range) // (digit_count - 1)
        number = str(10 ** (power - 1) + offset_number)

        # 计算在该数字中的具体位置
        offset_digit = (digit - start_range) % (digit_count - 1)
        results.append(number[offset_digit])

    # 输出从 1 到 n 的所有结果，每行一个
    for r in results:
        print(r)


if __name__ == "__main__":
    # 示例：调用 main(20)
    main(20)