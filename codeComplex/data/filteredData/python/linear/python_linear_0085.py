import random

def chain_reaction(n, beacons):
    table = [0] * n
    # table[i] represents the number of beacons destroyed if the first i beacons are used
    for i in range(n):
        position = beacons[i][0]
        power = beacons[i][1]
        destroyed = 0
        r = position - power

        # binary search to find the index of the last beacon with position < r
        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if beacons[mid][0] < r:
                lo = mid + 1
            else:
                hi = mid - 1

        # beacons destroyed by previously activated one (if any)
        if hi >= 0:
            destroyed += table[hi]
        # beacons destroyed by currently activated one
        destroyed += (i - (hi + 1))
        table[i] = destroyed

    # calculate cost of placing a beacon that activates each beacon in the table
    options = []
    for i in range(n):
        if i == 0:
            # when i == 0, there is no table[i-1]; original logic effectively treats it as 0
            cost = (n - i)
        else:
            cost = (n - i) + table[i - 1]
        options.append(cost)

    min_cost = min(options)

    # options: add a beacon that doesn't destroy any or add a beacon that destroys the beacon with minimum cost
    return min(table[n - 1], min_cost)


def generate_test_data(n):
    """
    生成规模为 n 的测试数据：
    - 位置为严格递增的整数
    - 功率为非负整数，不超过某个上界
    """
    beacons = []
    position = 0
    max_step = 10**6 // max(1, n)  # 控制位置范围不要太大
    for _ in range(n):
        step = random.randint(1, max_step if max_step > 0 else 1)
        position += step
        power = random.randint(0, position)  # 功率不超过当前位置
        beacons.append((position, power))
    beacons.sort()
    return beacons


def main(n):
    # 根据 n 生成测试数据
    beacons = generate_test_data(n)
    # 调用原有逻辑
    result = chain_reaction(n, beacons)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main，实际使用时可由外部传入 n
    main(10)