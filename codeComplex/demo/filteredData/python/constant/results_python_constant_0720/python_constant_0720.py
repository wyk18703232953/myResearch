def main(n: int):
    # 这里将 n 视为原程序中的 k，即第 n 个数字（从 1 开始计数）
    k = n

    prev = 0
    nextt = 0
    NumofDigits = 0

    # 寻找 k 所在的位数区间
    while True:
        prev = nextt
        nextt = nextt + (9 * (10 ** (NumofDigits - 1)) * NumofDigits)
        if prev <= k <= nextt:
            break
        NumofDigits += 1

    # 处理一位数和多位数情况
    if NumofDigits == 1:
        # 一位数直接输出 k（假设从 1-9 对应 k=1..9）
        # print(k)
        pass

    else:
        # 找到 k 落在的具体那个数
        result = (10 ** (NumofDigits - 1)) + int((k - (prev + 1)) / NumofDigits)

        # 确定是该数的第几位
        i = 0
        while True:
            if (k - int(prev + 1)) % NumofDigits == i:
                break
            i += 1

        result = str(result)
        # print(result[i])
        pass
if __name__ == "__main__":
    # 示例：自动生成一个测试规模 n 来调用 main
    # 可以根据需要修改生成测试数据的方式
    test_n = 100  # 比如取第 100 个数字
    main(test_n)