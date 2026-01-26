import sys


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


def core_logic(n, m, boys, girls):
    firstMax = max(boys)
    secondMax = second_largest(boys)
    minGrills = min(girls)
    if firstMax > minGrills:
        return -1
    elif firstMax == minGrills:
        minSum = m * (sum(boys) - firstMax) + sum(girls)
    elif n == 1:
        return -1

    else:
        minSum = m * sum(boys) + sum(girls) - (m - 1) * firstMax - secondMax
    return minSum


def generate_data(n):
    if n <= 0:
        n = 1
    # n 作为男生人数；女生人数 m = n + 1，确保 m >= 2
    boys_count = n
    girls_count = n + 1
    m = girls_count

    # 生成确定性 boys 列表：1, 2, ..., boys_count
    boys = [i + 1 for i in range(boys_count)]

    # 生成确定性 girls 列表：i % boys_count + 1，保证值不小于 1
    girls = [(i % boys_count) + 1 for i in range(girls_count)]

    return boys_count, m, boys, girls


def main(n):
    n_boys, m, boys, girls = generate_data(n)
    result = core_logic(n_boys, m, boys, girls)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的规模
    main(10)