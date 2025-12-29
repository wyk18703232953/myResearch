from math import sqrt
import random


def main(n: int):
    """
    n 作为规模参数，用于生成测试数据。
    这里简单地让加速度和速度等与 n 有关，保证量级随 n 变化。
    """
    # 生成测试数据（可根据需要调整生成策略）
    # 保证参数为正数，并满足一定物理意义（例如距离为正）
    a = max(1, n)                  # 加速度
    vm = max(1, n // 2 + 1)        # 最大速度
    l = max(1, n * 10)             # 总距离
    d = max(1, n * 5)              # 限速路段长度（可小于或大于 l，这里不强制关系）
    vd = max(1, n // 3 + 1)        # 限速

    # 原逻辑开始
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

    print(f"{ans:.12f}")


if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)