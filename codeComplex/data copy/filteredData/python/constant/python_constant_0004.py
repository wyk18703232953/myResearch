from math import sqrt

def main(n):
    # 映射 n 到一组确定性的参数 (a, vm, l, d, vd)
    # 保证都是正整数，且随 n 逐步变化
    a = n % 7 + 1           # 1..7
    vm = n * 2 + 3          # 3,5,7,...
    l = n * n + 10          # 随 n 二次增长
    d = (n * 3) // 2 + 5    # 5,6,8,9,...
    vd = n % 5 + 1          # 1..5

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
    return ans

if __name__ == "__main__":
    main(10)