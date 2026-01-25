def main(n):
    # n 表示数组长度
    if n <= 0:
        # 原代码假设至少有一个输入，因此这里直接返回一种固定情况
        print('cslnb')
        return

    # 构造确定性的输入数组 a，长度为 n
    # 设计：a[i] = i // 2，保证存在重复元素，且随 n 变化规模自然扩大
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
    # 示例调用，可根据需要修改 n 进行规模实验
    main(10)