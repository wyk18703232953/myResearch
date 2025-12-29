from math import sqrt
import random


def main(n: int):
    # 根据规模 n 生成测试数据：
    # a, vm, l, d, vd 都在 1 ~ n 之间（简单的一种生成方式）
    # 保证不为 0，以避免除零。
    if n < 1:
        n = 1

    a = random.randint(1, n)
    vm = random.randint(1, n)
    l = random.randint(1, n)
    d = random.randint(1, n)
    vd = random.randint(1, n)

    # 原始逻辑
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

    print('%.12f' % ans)


if __name__ == "__main__":
    # 示例：使用 n = 100 运行一次
    main(100)