def gett(a, b, c):
    delta = b ** 2 - 4 * a * c
    t1 = (-b + delta ** 0.5) / (2 * a)
    t2 = (-b - delta ** 0.5) / (2 * a)
    if min(t1, t2) > 0:
        return min(t1, t2)

    else:
        return max(t1, t2)


def experiment_case(a, v, l, d, w):
    t = 0.0
    if 2 * a * d <= w * w or v <= w:
        if 2 * a * l <= v * v:
            t = (2 * l / a) ** 0.5

        else:
            t = l / v + v / a / 2

    else:
        tmp = d - 0.5 * v * v / a + 0.5 * (v - w) ** 2 / a - v * (v - w) / a
        if tmp <= 0:
            tmp2 = l - d - (0.5 * (v - w) ** 2 / a + w * (v - w) / a)
            if tmp2 >= 0:
                t = tmp2 / v + (v - w) / a + 2 * gett(a, 2 * w, w * w / (2 * a) - d) + w / a

            else:
                t = gett(a / 2, w, d - l) + 2 * gett(a, 2 * w, w * w / (2 * a) - d) + w / a

        else:
            tmp2 = l - d - (0.5 * (v - w) ** 2 / a + w * (v - w) / a)
            if tmp2 >= 0:
                t = tmp2 / v + (v - w) / a + (2 * v - w) / a + tmp / v

            else:
                t = gett(a / 2, w, d - l) + (2 * v - w) / a + tmp / v
    return t


def main(n):
    if n <= 0:
        return

    # 确定性生成 n 组输入数据：
    # 对第 i 组（1 <= i <= n）：
    # a_i = 1 + (i % 5)
    # v_i = 1 + (2 * i % 7)
    # l_i = 10 + 3 * i
    # d_i = 5 + 2 * i
    # w_i = 1 + (3 * i % 9)
    results = []
    for i in range(1, n + 1):
        a = 1 + (i % 5)
        v = 1 + (2 * i % 7)
        l = 10 + 3 * i
        d = 5 + 2 * i
        w = 1 + (3 * i % 9)
        # 保证部分物理意义上合理的关系，简单裁剪
        if d > l:
            d = l // 2 if l >= 2 else l
        t = experiment_case(a, v, l, d, w)
        results.append(t)

    for t in results:
        # print(f"{t:.12f}")
        pass
if __name__ == "__main__":
    main(10)