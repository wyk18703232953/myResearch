import random

def chain_reaction(n, beacons):
    table = [0] * n
    # table[i] represents the number of beacons destroyed if the first i beacons are used
    for i in range(n):
        position = beacons[i][0]
        power = beacons[i][1]
        destroyed = 0
        r = position - power
        # use binary search to find the beacon that will be activated after the current one
        lo = 0
        hi = len(beacons) - 1
        while lo <= hi:
            mid = int(lo + (hi - lo) / 2)
            if beacons[mid][0] < r:
                lo = mid + 1
            else:
                hi = mid - 1
        # beacons destroyed by next activated one
        if hi >= 0:
            destroyed += table[hi]
        # beacons destroyed by currently activated one
        destroyed += (i - (hi + 1))
        table[i] = destroyed

    # find first index of max # of beacons destroyed
    max_val = max(table)
    ind = 0
    while ind < len(table):
        if table[ind] == max_val:
            break
        ind += 1
    cost = (len(table) - ind) + table[ind - 1]

    options = []
    for i in range(n):
        cost = (n - i) + table[i - 1]
        options.append(cost)
    min_cost = min(options)

    return min(table[n - 1], min_cost)


def main(n):
    # 生成测试数据：n 个灯塔，每个灯塔位置和能量为正整数
    # 这里简单生成：位置为 1..n 的随机排列，能量为 0..n 范围内的随机值
    positions = random.sample(range(1, 10 * n + 1), n)
    beacons = [(pos, random.randint(0, 10 * n)) for pos in positions]
    beacons.sort()
    result = chain_reaction(n, beacons)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)