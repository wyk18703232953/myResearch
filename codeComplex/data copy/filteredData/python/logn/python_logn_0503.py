def main(n: int):
    """
    n: 测试规模，用于生成第 n 个查询位置 k（从 1 开始计数）。
    本例中我们直接令 k = n，表示查询无限数字序列中的第 n 位数字：
    1234567891011121314...
    """
    k = n  # 根据规模生成测试数据，这里简单设为 k = n

    # 原逻辑开始
    num_digits = 1
    num_numbers = 9

    k -= 1  # 转为从 0 开始计数
    while k > num_digits * num_numbers:
        k -= num_numbers * num_digits
        num_digits += 1
        num_numbers *= 10

    number = 10 ** (num_digits - 1) + k // num_digits
    index = k % num_digits
    answer = str(number)[index]
    # print(answer)
    pass
if __name__ == "__main__":
    # 示例：调用 main(15) 即求无限序列的第 15 位
    main(15)