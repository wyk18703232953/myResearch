def main(n: int):
    # 使用 n 作为原代码中的 k
    k = n

    if k <= 9:
        print(k)
        return
    else:
        length = len(str(k))
        s = ""
        num = 0

        for i in range(length - 1):
            num += (9 * (10 ** i)) * (i + 1)
            temp = num + (9 * (10 ** (i + 1))) * (i + 2)
            if temp > k:
                length = i + 2
                break

        for i in range(length - 1):
            s = s + "1"

        previous_value = 9 * int(s)
        try_value = k - num

        if try_value % length == 0:
            div_value = try_value // length
            temp_string = str(previous_value + div_value)
            print(temp_string[len(temp_string) - 1])
        else:
            div_value = (try_value // length) + 1
            temp_string = str(previous_value + div_value)
            differ = (div_value * length) - try_value
            print(temp_string[len(temp_string) - differ - 1])


# 示例：根据规模 n 生成测试数据并调用主逻辑
if __name__ == "__main__":
    # 这里根据规模 n 生成测试数据；简单起见，直接用 n 本身作为 k
    # 可以修改为其它生成策略，如 k = 10**n - 1 等
    for n in [1, 5, 9, 10, 15, 100, 1000]:
        print(f"n = {n}, output = ", end="")
        main(n)