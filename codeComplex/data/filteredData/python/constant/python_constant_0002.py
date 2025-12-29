from math import sqrt
import random


def main(n: int):
    # 1. 根据规模 n 生成测试数据
    # 这里示例性地将 n 当作最大取值范围的控制参数
    # 可按需要修改生成策略
    if n <= 0:
        n = 1

    # 随机生成参数，保证物理含义大致合理
    # a: 加速度（>0）
    # vm: 最大速度（>0）
    # l: 赛道总长度（>0）
    # d: 限速路段长度（0 < d < l）
    # vd: 限速路段最大速度（>0）
    a = random.uniform(0.1, n)
    vm = random.uniform(0.1, n)
    l = random.uniform(1.0, 10.0 * n)
    d = random.uniform(0.1, max(0.2, l * 0.8))
    vd = random.uniform(0.1, n)

    # 2. 原始逻辑（去掉 input），直接使用生成的 a, vm, l, d, vd
    if vm <= vd or sqrt(2 * a * d) <= vd:
        if vm ** 2 / (2 * a) >= l:
            ans = sqrt(2 * l / a)
        else:
            ans = vm / a + (l - vm ** 2 / (2 * a)) / vm
    else:
        s1 = (vm ** 2 - vd ** 2) / (2 * a)
        if s1 >= (l - d):
            ans = (sqrt(4 * (vd ** 2) + 8 * a * (l - d)) - 2 * vd) / (2 * a)
        else:
            ans = (vm - vd) / a + (l - d - s1) / vm
        v1 = sqrt((2 * a * d + vd ** 2) / 2)
        if v1 <= vm:
            ans = ans + v1 / a + (v1 - vd) / a
        else:
            s1 = d - (vm ** 2 - vd ** 2) / (2 * a) - (vm ** 2) / (2 * a)
            ans = ans + vm / a + (vm - vd) / a + s1 / vm

    # 3. 输出结果（与原程序格式一致）
    print(f"{ans:.12f}")


if __name__ == "__main__":
    # 示例调用，规模 n 可按需要修改
    main(10)