# -*- coding: utf-8 -*-

EPS = 1e-6


def solve_one_case(n, m, a, b):
    b = b + [b[0]]

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

    res = binary_search(0, 1e9 + 1)
    if res - 1e9 > EPS:
        return -1
    else:
        return float(f"{res:.10f}")


def main(n):
    """
    n: 问题规模，即数组 a,b 的长度。
    这里按以下策略生成测试数据：
      - m 固定为 1000
      - a[i], b[i] 均生成为 2 ~ 20 范围内的整数，以保证可行解较大概率存在
    """
    import random

    m = 1000
    # 确保每一段消耗不会过大，这里用相对较大的系数
    a = [random.randint(2, 20) for _ in range(n)]
    b = [random.randint(2, 20) for _ in range(n)]

    ans = solve_one_case(n, m, a, b)
    print(ans)


if __name__ == "__main__":
    # 示例：以 n = 5 运行一次
    main(5)