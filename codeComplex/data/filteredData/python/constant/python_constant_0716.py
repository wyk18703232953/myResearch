def main(n):
    k = n

    if k <= 9:
        # print(k)
        pass
        return

    num_arr = [9 * (i + 1) * 10 ** i for i in range(11)]
    index = 0

    while True:
        if k <= num_arr[index]:
            break

        else:
            k -= num_arr[index]
            index += 1

    digit = index + 1
    k += digit - 1

    num = k // digit
    offset = k % digit

    string_num = str(10 ** (digit - 1) + num - 1)

    # print(string_num[offset])
    pass
if __name__ == "__main__":
    # 示例：根据规模 n 生成测试数据，这里直接使用 n 本身作为 k
    # 可自行修改 n 的值进行测试
    test_n = 1000
    main(test_n)