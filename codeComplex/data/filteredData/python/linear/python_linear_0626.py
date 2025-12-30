import random


def main(n: int):
    # 1. 生成测试数据
    # n 表示总人数（骑手 + 普通居民），至少需要 1 个骑手
    if n < 1:
        return

    # 生成房屋位置：随机不重复整数并排序，使之更贴近原题场景
    houses = sorted(random.sample(range(1, 3 * n + 1), n))

    # 生成是否为骑手的标记：保证至少有一个骑手
    is_rider = [0] * n
    # 随机挑选若干人为骑手（至少 1 个）
    rider_count = random.randint(1, n)
    rider_indices = random.sample(range(n), rider_count)
    for idx in rider_indices:
        is_rider[idx] = 1

    # 2. 原始逻辑
    current_left_driver = None
    current_citizens = []
    result = []

    for house, r in zip(houses, is_rider):
        if r:
            if current_left_driver is None:
                # 第一个骑手前面的居民全部计入当前骑手
                result.append(len(current_citizens))
            else:
                # 存在左侧骑手，需要对区间内的居民做最近骑手划分
                result.append(0)  # 先给左骑手的计数位
                for citizen in current_citizens:
                    if abs(citizen - current_left_driver) <= abs(citizen - house):
                        result[-2] += 1
                    else:
                        result[-1] += 1

            current_citizens = []
            current_left_driver = house
        else:
            current_citizens.append(house)

    # 最后一个骑手右侧的所有居民都归这个骑手
    if result:  # 至少有一个骑手
        result[-1] += len(current_citizens)

    # 3. 输出结果
    print(' '.join(map(str, result)))


if __name__ == "__main__":
    # 示例：可根据需要调整 n
    main(10)