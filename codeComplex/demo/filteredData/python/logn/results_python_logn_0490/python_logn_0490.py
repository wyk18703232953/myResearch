def main(n: int):
    k = n  # 使用 n 作为原程序中的 k

    if k <= 9:
        # print(k)
        pass
        return

    else:
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
    # 示例：根据需要调用 main(n) 进行测试
    # 这里给出一个简单的示例调用
    main(15)