def main(n: int):
    # 生成测试数据：这里直接使用 n 作为原程序中的 k
    k = int(n)

    n_digit = 1
    # 找到第 k 位所在的“位数段”
    while k - n_digit * 9 * (10 ** (n_digit - 1)) > 0:
        k -= n_digit * 9 * (10 ** (n_digit - 1))
        n_digit += 1

    n_digit -= 1  # 修正到实际位数

    if n_digit == 0:
        print(k)
    else:
        # 当前段中第 nth_num 个数
        nth_num = (k - 1) // (n_digit + 1) + 1
        num = 10 ** n_digit + nth_num - 1
        pos = (k - 1) % (n_digit + 1)
        print(int(str(num)[pos]))


if __name__ == "__main__":
    # 示例：调用 main(1000) 可测试第 1000 位
    main(1000)