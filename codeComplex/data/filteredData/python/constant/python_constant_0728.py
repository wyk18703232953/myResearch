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
            print(''.join(list(reversed(str(difference))))[position])
            break
        else:
            decimal = int(str(limit_int) * (count + 1))
            limit += int(str(limit_int) + '0' * count) * (count + 1)


# 示例：根据规模 n 生成测试数据并调用 main
if __name__ == "__main__":
    # 这里简单地使用 n 本身作为测试数据的规模控制
    # 调用时可自行修改为需要的 n
    test_n = 100  # 示例规模，可按需要调整
    main(test_n)