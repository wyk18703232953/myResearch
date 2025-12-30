import random

def main(n):
    # 生成规模为 n 的测试数据
    # 规则：
    # 1) m 为司机数量，1 <= m <= n，且不为 0
    # 2) distances 为 1..n 的一个排列
    # 3) taxiDriver 为长度 n 的 0/1 数组，恰有 m 个 1
    m = random.randint(1, n)

    distances = list(range(1, n + 1))
    random.shuffle(distances)

    taxiDriver = [0] * n
    driver_positions = random.sample(range(n), m)
    for pos in driver_positions:
        taxiDriver[pos] = 1

    people = []
    drivers = []
    result = [0] * m

    for i in range(len(distances)):
        if taxiDriver[i]:
            drivers.append(distances[i])
        else:
            people.append(distances[i])

    # 对司机按距离排序，同时记录其原始索引，以便将乘客数量放到 result 对应位置
    indexed_drivers = list(enumerate(drivers))
    indexed_drivers.sort(key=lambda x: x[1])
    sorted_driver_positions = [idx for idx, _ in indexed_drivers]
    sorted_drivers = [dist for _, dist in indexed_drivers]

    people.sort()

    j = 0
    for person in people:
        if (j + 1) < len(sorted_drivers):
            while (j + 1) < len(sorted_drivers) and (sorted_drivers[j] - person) < (person - sorted_drivers[j + 1]):
                j += 1
            result[sorted_driver_positions[j]] += 1
        else:
            result[sorted_driver_positions[j]] += 1

    print(' '.join(map(str, result)))


if __name__ == "__main__":
    # 示例调用
    main(10)