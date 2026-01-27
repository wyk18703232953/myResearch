from math import sqrt

def main(n):
    # 确定性构造输入参数
    # 保证各参数为正数并具有一定变化，以覆盖不同分支
    a = n % 7 + 1          # 加速度
    vm = n % 11 + 5        # 最大速度
    l = n * 3 + 10         # 总路程
    d = max(1, n // 2)     # 需要减速的起点位置
    vd = n % 9 + 2         # 限速区最大速度

    # 原算法逻辑
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

    # print('%.12f' % ans)
    pass
if __name__ == "__main__":
    main(100000)