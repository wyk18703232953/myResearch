def main(n):
    # n 表示数组长度
    if n <= 0:
        return

    # 确定性生成长度为 n 的整数数组
    # 构造方式：a[i] = i // 2，保证存在一些重复，规模随 n 线性增长
    a = [i // 2 for i in range(n)]

    a = sorted(a)
    duplicates = {}
    d = None
    delta = 0
    for i, el in enumerate(a, 1):
        if el not in duplicates:
            duplicates[el] = 0
        else:
            d = el
            duplicates[el] += 1
        min_value = i - 1
        delta += el - min_value

    if sum(duplicates.values()) > 1 or duplicates.get(0, 0) >= 1 or (d is not None and d - 1 in duplicates):
        print('cslnb')
    elif delta == 0:
        print('cslnb')
    elif delta % 2 == 1:
        print('sjfnb')
    else:
        print('cslnb')


if __name__ == "__main__":
    # 示例：使用 n = 10 作为输入规模
    main(10)