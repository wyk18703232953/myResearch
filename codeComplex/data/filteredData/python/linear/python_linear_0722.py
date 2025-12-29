import sys
import random


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
    # 生成规模为 n 的测试数据
    # n: 男孩数量
    # m: 女孩数量，设为 n 或 n+1 以保证多样性
    if n <= 0:
        print(-1)
        return

    m = max(1, n + 1)

    # 生成分数，范围可自行调整
    # 保证整数且有一定重复概率
    boys = [random.randint(1, 100) for _ in range(n)]
    girls = [random.randint(1, 100) for _ in range(m)]

    firstMax = max(boys)
    secondMax = second_largest(boys)
    minGrills = min(girls)

    if firstMax > minGrills:
        print(-1)
        return
    elif firstMax == minGrills:
        minSum = m * (sum(boys) - firstMax) + sum(girls)
    elif n == 1:
        print(-1)
        return
    else:
        minSum = m * sum(boys) + sum(girls) - (m - 1) * firstMax - secondMax

    print(minSum)


if __name__ == "__main__":
    # 示例：调用 main，n 可按需修改
    main(5)