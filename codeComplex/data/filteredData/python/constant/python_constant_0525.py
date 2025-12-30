import random

def main(n: int):
    # 生成测试数据：
    # 为了体现规模 n，这里生成 n 组不同的 (x, y, z, t1, t2, t3)
    # 并对每组数据执行原有逻辑。
    #
    # 取值策略（可按需调整）：
    #   楼层范围：0 ~ n
    #   时间参数：1 ~ 10
    #
    # 返回所有结果，便于测试或断言。
    results = []
    for _ in range(n):
        x = random.randint(0, n)
        y = random.randint(0, n)
        z = random.randint(0, n)
        t1 = random.randint(1, 10)
        t2 = random.randint(1, 10)
        t3 = random.randint(1, 10)

        lift_time = (abs(z - x) + abs(y - x)) * t2 + 3 * t3
        stairs_time = abs(y - x) * t1

        if lift_time <= stairs_time:
            result = "YES"
        else:
            result = "NO"

        # 打印每组数据及结果，便于查看
        print(x, y, z, t1, t2, t3, "->", result)
        results.append((x, y, z, t1, t2, t3, result))

    return results

if __name__ == '__main__':
    # 示例：运行规模为 5 的测试
    main(5)