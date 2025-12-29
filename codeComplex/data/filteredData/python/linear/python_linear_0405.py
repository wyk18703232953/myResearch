from math import ceil
import random

def main(n):
    # 1. 生成测试数据
    # 为保证可行性，生成 strictly increasing 的 lift 和 land 且 land[0] = lift[-1]
    # 这样存在一个有限解，二分不会全部失败为 -1
    base = 2
    step = 1

    lift = [base + i * step for i in range(n)]
    land = lift[1:] + [lift[0]]  # land[i+1] 存在，且 land[0] = lift[-1]

    # 2. 设置 total_wgt 和 r1
    total_wgt = 10
    r1 = total_wgt

    # 3. 补上循环使用的首元素（与原代码一致）
    lift_ext = lift + [lift[0]]
    land_ext = land + [land[0]]

    def test(f):
        # 使用外部闭包变量：r1, lift_ext, land_ext, n
        for i in range(n):
            if (r1 + f) > f * lift_ext[i]:
                return 0
            f -= (r1 + f) / lift_ext[i]
            if (r1 + f) > f * land_ext[i + 1]:
                return 0
            f -= (r1 + f) / land_ext[i + 1]
        return 1

    # 4. 原逻辑的二分搜索部分
    l = 0.0
    r = 1e20
    for _ in range(1000):
        mid = (l + r) / 2.0
        if test(mid):
            r = mid
        else:
            l = mid

    if r < 1e19:
        print('%.17f' % r)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：n = 5
    main(5)