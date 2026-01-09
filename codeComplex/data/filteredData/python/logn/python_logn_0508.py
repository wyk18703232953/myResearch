def main(n: int):
    # 将原来的 index 视为“规模”为 n 的测试数据：直接用 n 作为 index
    index = n

    total = 9
    digit_len = 1

    # 找到 index 落在多少位数的区间
    while index > total:
        total += (digit_len + 1) * (10 ** digit_len) * 9
        digit_len += 1

    last = 10 ** (digit_len - 1)
    total -= digit_len * 9 * last
    index = index - total

    r = index % digit_len
    k = index // digit_len

    number = last + k

    if r == 0:
        # print(str(number - 1)[digit_len - 1])
        pass

    else:
        # print(str(number)[r - 1])
        pass
if __name__ == "__main__":
    # 示例：调用 main(15)，表示 index=15
    main(15)