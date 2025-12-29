from math import sqrt


def main(n):
    # 根据规模 n 生成测试数据：
    # 简单策略：让加速度、初速度、距离等随 n 变化，避免退化为常量
    a = 1 + n * 0.1          # 加速度
    vm = 5 + n               # 最大速度
    l = 100 + 10 * n         # 总距离
    d = max(1.0, l * 0.3)    # 在 d 处可能有速度限制
    vd = max(1.0, vm * 0.6)  # 受限速度

    # 下面是原逻辑，只是把输入改为使用上述生成的数据
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
    return ans


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)