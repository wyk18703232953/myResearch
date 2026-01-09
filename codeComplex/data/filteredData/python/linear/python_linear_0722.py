def second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1

            else:
                m2 = x
    return m2 if count >= 2 else None


def main(n):
    # 映射：n -> (n, m) 且 m >= 1
    # 为了可规模化，将 m 设为 n（至少为 1）
    if n <= 0:
        return None

    boys_count = n
    girls_count = n
    m = n

    # 构造确定性 boys 和 girls 数据
    # boys 为长度 n 的整数列表，元素随索引线性增长
    boys = [i % (n + 3) + 1 for i in range(boys_count)]
    # 确保 boys 中有至少两个不同值，以符合 second_largest 的语义
    if boys_count >= 2:
        boys[0] = 1
        boys[1] = 2

    # girls 为长度 n 的整数列表，元素也随索引线性变化但与 boys 不同模式
    girls = [(i * 2) % (n + 5) + 1 for i in range(girls_count)]

    firstMax = max(boys)
    secondMax = second_largest(boys)
    minGrills = min(girls)
    minSum = 0

    if firstMax > minGrills:
        result = -1
    elif firstMax == minGrills:
        result = m * (sum(boys) - firstMax) + sum(girls)
    elif boys_count == 1:
        result = -1

    else:
        result = m * sum(boys) + sum(girls) - (m - 1) * firstMax - secondMax

    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模参数
    main(10)