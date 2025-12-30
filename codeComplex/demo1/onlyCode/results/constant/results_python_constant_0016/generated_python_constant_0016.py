from math import sqrt


def main(n):
    # 根据规模 n 生成测试数据：
    # a, v, l, d, w 都随 n 线性增长，保证为正数
    a = max(1, n)           # 加速度
    v = max(1, 2 * n)       # 最大速度
    l = max(2, 5 * n)       # 总路程
    d = max(1, l // 2)      # 限速区间结束位置（不超过总路程）
    w = max(1, n)           # 限速区间最大允许速度

    # 原逻辑开始
    w = min(v, w)
    lowtime = (v - w) / a
    lowdist = v * lowtime - a * lowtime ** 2 / 2
    startdist = v ** 2 / (2 * a)

    if startdist + lowdist <= d:
        ans = v / a + (d - startdist - lowdist) / v + lowtime
    elif w ** 2 <= 2 * d * a:
        u = sqrt(a * d + w ** 2 / 2)
        ans = (2 * u - w) / a
    else:
        ans = sqrt(2 * d / a)
        w = ans * a

    hightime = (v - w) / a
    highdist = w * hightime + a * hightime ** 2 / 2

    if highdist <= l - d:
        ans += hightime + (l - d - highdist) / v
    else:
        disc = sqrt(w ** 2 + 2 * a * (l - d))
        ans += (disc - w) / a

    print(f"{ans:.7f}")


if __name__ == "__main__":
    # 示例：使用 n=10 运行一次
    main(10)