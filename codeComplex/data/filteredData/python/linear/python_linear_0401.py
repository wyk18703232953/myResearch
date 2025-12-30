# -*- coding: utf-8 -*-
# 转换版：去除 input()，使用 main(n) 生成测试数据并运行

EPS = 1e-6


def solve(n, m, a, b):
    b = b[:]  # 避免修改原列表
    b.append(b[0])

    def check(f):
        fuel_left = f
        total_weight = float(m + fuel_left)
        for i in range(n):
            cost = total_weight / a[i]
            fuel_left -= cost
            total_weight -= cost

            cost = total_weight / b[i + 1]
            fuel_left -= cost
            total_weight -= cost

            if fuel_left < 0:
                return False
        return True

    def binary_search(left, right):
        mid = (left + right) / 2
        if abs(left - right) < EPS:
            return mid
        if check(mid):
            return binary_search(left, mid)
        else:
            return binary_search(mid, right)

    res = binary_search(0.0, 1e9 + 1.0)
    if res - 1e9 > EPS:
        return -1
    return res


def main(n):
    """
    根据规模 n 生成一组合理的测试数据并运行算法。
    n: 飞行段数（原题中与数组 a, b 的长度相对应）
    返回：算法输出结果（若无解返回 -1，否则为最小所需燃料）
    """
    # 生成测试数据策略：
    # - m：飞机自重（不含燃料），取一个中等整数
    # - a[i], b[i]：每一段的燃油效率参数，需保证都 > 1 才有意义
    import random

    random.seed(0)

    # 飞机空重
    m = 1000

    # a 和 b 均为长度 n 的数组，每个值在 [2, 20] 之间
    a = [random.randint(2, 20) for _ in range(n)]
    b = [random.randint(2, 20) for _ in range(n)]

    result = solve(n, m, a, b)

    # 输出结果（保持与原程序风格一致）
    if result == -1:
        print(-1)
    else:
        print(f"{result:.10f}")

    # 也可以返回结果，方便在其他地方调用
    return result


if __name__ == "__main__":
    # 示例：使用 n = 5 运行一次
    main(5)