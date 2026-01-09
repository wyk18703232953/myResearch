def main(n: int):
    limit_int = limit = decimal = 9
    count = 0
    while True:
        count += 1
        if n <= limit:
            difference = limit - n
            position = difference % count
            difference = difference // count
            difference = decimal - difference
            # print(''.join(list(reversed(str(difference))))[position])
            pass
            break

        else:
            decimal = int(str(limit_int) * (count + 1))
            limit += int(str(limit_int) + '0' * count) * (count + 1)


if __name__ == "__main__":
    # 示例：根据需要设置 n 的测试值
    test_n = 100
    main(test_n)