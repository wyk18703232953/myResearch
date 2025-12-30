def main(n):
    # 本题原逻辑中原始输入为 k，这里用 n 作为规模及 k 的值
    k = int(n)

    if k < 10:
        print(k)
        return

    c = 0
    a = k
    while True:
        c += 1
        sub = 10 ** c - 10 ** (c - 1)
        a -= sub * c
        # 按原程序使用浮点除法
        current_n = a / (c + 1) + (10 ** c - 1)

        if current_n + 1 <= 10 ** (c + 1):
            if int(current_n) == current_n:  # 整数
                print(int(current_n % 10))
                return
            else:
                # 非整数时，原逻辑取 (c+1) 位数字中的某一位
                idx = round((current_n - int(current_n)) * (c + 1)) - 1
                print(str(int(current_n) + 1)[idx])
                return


if __name__ == "__main__":
    # 示例：根据规模 n 生成测试数据
    # 这里直接用 n 作为 k 的值。可以按需要修改为其他生成方式。
    test_n = 1000
    main(test_n)