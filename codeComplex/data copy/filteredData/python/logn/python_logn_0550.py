def main(n):
    # 这里将 n 作为原程序中的 k 使用
    k = n

    prev = 0
    next_val = 0
    NumofDigits = 0

    while True:
        prev = next_val
        next_val = next_val + (9 * (10 ** (NumofDigits - 1)) * NumofDigits)
        if prev <= k <= next_val:
            break
        NumofDigits += 1

    if NumofDigits == 1:
        # print(k)
        pass

    else:
        result_num = (10 ** (NumofDigits - 1)) + int((k - (prev + 1)) / NumofDigits)
        i = 0
        while True:
            if (k - int(prev + 1)) % NumofDigits == i:
                break
            i += 1
        result_str = str(result_num)
        # print(result_str[i])
        pass
if __name__ == "__main__":
    # 示例：根据规模 n 生成测试数据，这里直接用 n 自身作为 k
    # 可根据需要调整，如 main(100), main(1000) 等
    main(100)